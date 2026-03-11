import sqlite3
from logic import Event

DATABASE = "scheduler.db"

def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # lets us access columns by name instead of index
    return conn

def init_db():
    """Create the events table if it doesn't exist yet."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id TEXT PRIMARY KEY,
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

def save_event(event):
    """Insert a new event into the database."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (id, title, day, start, end, location, priority)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        event.id,
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
    """Delete an event from the database by its ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))

    conn.commit()
    conn.close()

def load_all_events():
    """Load all events from the database and return them as Event objects."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events")
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
        event.id = row["id"]  # restore the original ID, don't generate a new one
        events.append(event)

    return events