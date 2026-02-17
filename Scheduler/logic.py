from datetime import datetime

time_pattern = r'^\d{1,2}:\d{1,2}$'
days_of_week = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
id_tags = []


class TimeConflict(Exception):
    """Exception raised when two events conflict.

    Attributes:
        new_event -- the event being added (optional)
        existing_event -- the event already scheduled that conflicts (optional)
        message -- human-readable description
    """
    def __init__(self, new_event=None, existing_event=None):
        self.new_event = new_event
        self.existing_event = existing_event
        if new_event is None or existing_event is None:
            # Generic conflict (e.g., invalid duration)
            self.message = "Time conflict detected."
        else:
            # Determine priority ordering (lower number = higher priority)
            new_pr = getattr(new_event, 'priority', None)
            ex_pr = getattr(existing_event, 'priority', None)
            self.message = (
                f"Conflict between '{new_event.title}' (priority={new_pr}) "
                f"and '{existing_event.title}' (priority={ex_pr})."
            )
        super().__init__(self.message)


class Day:
    def __init__(self, day: str):
        if day.lower() not in days_of_week:
            raise IndexError
        self.day_name = day
        self.number = days_of_week[day.lower()]
        self.events = []

    def has_conflict(self, new_event):
        # Verify new event doesn't conflict with existing events
        for existing in self.events:
            if new_event.start_time < existing.end_time and new_event.end_time > existing.start_time:
                # Return the existing event that conflicts so callers can inspect/resolve
                return existing
        return None

    def add_event(self, event):
        conflict = self.has_conflict(event)
        if not conflict:
            self.events.append(event)
            self.events.sort(key=lambda e: e.start_time)
            return

        # If there is a conflict, try to auto-resolve by priority.
        # Convention: lower priority number means higher priority (1 highest).
        try:
            new_pr = event.priority
            ex_pr = conflict.priority
        except AttributeError:
            # If priority not present, cannot auto-resolve
            raise TimeConflict(event, conflict)

        if new_pr < ex_pr:
            # New event has higher priority: replace the existing event
            try:
                self.events.remove(conflict)
            except ValueError:
                # Shouldn't happen, but treat as conflict
                raise TimeConflict(event, conflict)
            self.events.append(event)
            self.events.sort(key=lambda e: e.start_time)
            print(f"{conflict.title} was removed in favor of {event.title} by priority")
            return

        # Existing event has equal or higher priority -> raise conflict with details
        raise TimeConflict(event, conflict)

    def remove_event(self, event):
        if len(self.events) > 0:  # no events to remove
            if event in self.events:
                self.events.remove(event)
                self.events.sort(key=lambda e: e.start_time)
            else:
                raise KeyError
        else:
            raise IndexError


    def list_events(self):
        return self.events

    def __str__(self):
        return self.day_name

    def __repr__(self):
        return self.day_name


# events need to have a date and location
class Event:
    def __init__(self, day: str, start_time: str, end_time: str,
                 title: str, location: str, tags: set[str] = None, priority: int = 4):
        self.day_num = days_of_week[day.lower()]
        self.location = location
        self.day = day
        self.priority = priority
        self.tags = tags
        self.title = title
        try:
            self.start_time = datetime.strptime(start_time, "%H:%M")
            self.end_time = datetime.strptime(end_time, "%H:%M")
        except:
            raise ValueError
        self.duration = self.end_time - self.start_time
        if self.duration.total_seconds() == 0 or self.start_time >= self.end_time:
            # Invalid event duration
            raise TimeConflict()

    def __str__(self):
        return f'{self.title}, at {self.location}, on {self.day}, at {self.start_time.hour}:{self.start_time.minute}'

    def __repr__(self):
        return (
            f"Event: {self.title}, for {self.duration.total_seconds() // 3600} hours,"
            f" at {self.start_time}, till {self.end_time}, "
            f"at {self.location}, on {self.day}")


class User:
    # User needs to be able to have default events as well as have a week and a timeline and a schedule
    def __init__(self, name):
        self.name = name
        self.week = [Day(x) for x in days_of_week]

    def add_default_event(self, event):
        pass
        # Work in progress

    def add_event(self, *args):
        for event in args:
            self.week[event.day_num].add_event(event)

    def __repr__(self):
        return self.name
