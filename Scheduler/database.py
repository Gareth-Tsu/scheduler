import sqlite3
import bcrypt
from logic import Event

DATABASE = "scheduler.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Events table — now with user_id linking to users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            title TEXT,
            day TEXT,
            start TEXT,
            end TEXT,
            location TEXT,
            priority INTEGER
        )
    """)

    conn.commit()
    conn.close()

def create_user(username, password):
    """Hash the password and insert a new user. Returns the new user's id."""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        user_id = cursor.lastrowid  # the auto-generated id of the new row
        return user_id
    except sqlite3.IntegrityError:
        # UNIQUE constraint failed — username already exists
        return None
    finally:
        conn.close()

def get_user_by_username(username):
    """Look up a user by username. Returns the row or None."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def check_password(stored_hash, password):
    """Check a plaintext password against a stored hash."""
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash)

def save_event(event, user_id):
    """Insert a new event linked to a user."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO events (id, user_id, title, day, start, end, location, priority)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        event.id,
        user_id,
        event.title,
        event.day,
        event.start_time.strftime("%H:%M"),
        event.end_time.strftime("%H:%M"),
        event.location,
        event.priority
    ))
    conn.commit()
    conn.close()

def delete_event(event_id):
    """Delete an event by its ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()
    conn.close()

def get_event_by_id(event_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_event(event):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE events SET title=?, day=?, start=?, end=?, location=?, priority=?
        WHERE id=?
    """, (
        event.title,
        event.day,
        event.start_time.strftime("%H:%M"),
        event.end_time.strftime("%H:%M"),
        event.location,
        event.priority,
        event.id
    ))
    conn.commit()
    conn.close()

def load_events_for_user(user_id):
    """Load all events belonging to a specific user."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()

    events = []
    for row in rows:
        event = Event(
            row["day"],
            row["start"],
            row["end"],
            row["title"],
            row["location"],
            row["priority"]
        )
        event.id = row["id"]
        events.append(event)

    return events