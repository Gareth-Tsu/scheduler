from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from logic import User, Event, TimeConflict
from database import (init_db, save_event, delete_event,
                      load_events_for_user, create_user,
                      get_user_by_username, check_password,
                      get_event_by_id, update_event)
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
init_db()

# --- Login Required Decorator ---

def login_required(func):
    @wraps(func)  # preserves the original function's name and info
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper


# --- Helper ---

def get_current_user():
    """Build a User object from the current session's saved events."""
    user = User(session["username"])
    for event in load_events_for_user(session["user_id"]):
        user.add_event(event)
    return user


# --- Auth Routes ---

@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = create_user(username, password)

        if user_id is None:
            return render_template("register.html", error="Username already taken")

        # Log them in immediately after registering
        session["user_id"] = user_id
        session["username"] = username
        return redirect(url_for("home"))

    return render_template("register.html", error=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_row = get_user_by_username(username)

        if user_row is None or not check_password(user_row["password"], password):
            return render_template("login.html", error="Invalid username or password")

        # Store user info in the session
        session["user_id"] = user_row["id"]
        session["username"] = user_row["username"]
        return redirect(url_for("home"))

    return render_template("login.html", error=None)


@app.route("/logout")
def logout():
    session.clear()  # wipe the session
    return redirect(url_for("login"))


# --- App Routes ---

@app.route("/")
@login_required
def home():
    user = get_current_user()
    return render_template("index.html", week=user.week, conflict=None,
                           username=session["username"])


@app.route("/add", methods=["POST"])
@login_required
def add_event():
    title = request.form["title"]
    day = request.form["day"]
    start = request.form["start"]
    end = request.form["end"]
    location = request.form["location"]
    priority = int(request.form["priority"])

    user = get_current_user()

    try:
        event = Event(day, start, end, title, location, priority)
        user.add_event(event)
        save_event(event, session["user_id"])

    except TimeConflict as e:
        return render_template("index.html", week=user.week, conflict=str(e),
                               username=session["username"])
    except ValueError:
        return render_template("index.html", week=user.week,
                               conflict="Invalid time format. Use HH:MM",
                               username=session["username"])
    except KeyError:
        return render_template("index.html", week=user.week,
                               conflict="Invalid day name.",
                               username=session["username"])

    return redirect(url_for("home"))


@app.route("/remove", methods=["POST"])
@login_required
def remove_event():
    event_id = request.form["event_id"]

    # Remove from database first
    delete_event(event_id, session["user_id"])

    return redirect(url_for("home"))

@app.route("/edit/<event_id>", methods=["GET", "POST"])
@login_required
def edit_event(event_id):
    if request.method == "GET":
        row = get_event_by_id(event_id, session["user_id"])
        if row is None:
            return redirect(url_for("home"))
        return render_template("edit.html", event=row)
    if request.method == "POST":
        title = request.form["title"]
        day = request.form["day"]
        start = request.form["start"]
        end = request.form["end"]
        location = request.form["location"]
        priority = int(request.form["priority"])

        user = get_current_user()
        try:
            event = user.edit_event(event_id, title=title, day=day,
                                    start_time=start, end_time=end,
                                    location=location, priority=priority)
            update_event(event)
        except (TimeConflict, KeyError) as e:
            row = get_event_by_id(event_id, session["user_id"])
            return render_template("edit.html", event=row, conflict=str(e))

        return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)