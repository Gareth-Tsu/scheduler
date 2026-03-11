from flask import Flask, render_template, request, redirect, url_for
from logic import User, Event, TimeConflict
from database import *
app = Flask(__name__)

init_db()

user = User("Me")
for event in load_all_events():
    user.add_event(event)

@app.route("/")
def home():
    return render_template("index.html", week=user.week, error=None)

@app.route("/remove", methods=["POST"])
def remove_event():
    event_id = request.form["event_id"]

    for day in user.week:
        event_to_remove = next((e for e in day.events if e.id == event_id), None)
        if event_to_remove:
            day.remove_event(event_to_remove)
            delete_event(event_id)
            break

    return redirect(url_for("home"))

@app.route("/add", methods=["POST"])
def add_event():
    # Read each form field by its name
    day        = request.form["day"]
    start_time = request.form["start_time"]
    end_time   = request.form["end_time"]
    title      = request.form["title"]
    location   = request.form["location"]
    priority   = int(request.form["priority"])

    try:
        event = Event(day, start_time, end_time, title, location, priority)
        user.add_event(event)
        save_event(event)
    except TimeConflict as e:
        # If there's a conflict, send the error message back to the page
        return render_template("index.html", week=user.week, error=str(e))
    except ValueError:
        return render_template("index.html", week=user.week, error="Invalid time format. Use HH:MM")

    # Success — reload the calendar
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)