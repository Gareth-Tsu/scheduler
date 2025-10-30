"""
weekly schedule planner
store all events
have a set of days with repeating events as default events 
have a weekly and daily timeline
"""
from datetime import datetime, timedelta

days_of_week = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
class Day:

    workdays = ['tuesday', 'thursday']
    def __init__(self, day: str):
        self.day_name = day
        self.number = days_of_week[day.lower()]
        self.events = []
        self.timeslots = {x: None for x in range(24)}
        if day.lower() in Day.workdays:
            shift = Event(self.day_name, [15, 0], [19, 0], 'Work', "Mister car wash")
            self.events.append(shift)
        if day.lower() == 'saturday':
            s = Event(self.day_name, [8, 0], [17, 0 ], 'Work', "Mister car wash")
            self.events.append(s)

    def add_event(self, event):
        if self.timeslots[(int(event.start_time.hour()))] is None:
            self.events.append(event)
            self.events.sort(key=lambda e: e.start_time)
            self.timeslots.update({int(event.start_time.hour()): event.title})

        else:
            raise RuntimeError("Event at that timeslot already")

    def remove_event(self, event):
        self.events.pop(event)
        self.timeslots += float(event.duration.total_seconds() // 3600)
        self.events.sort(key=lambda e: e.start_time)


    def list_events(self):
        return self.events
    # Each day needs to have 48 timeslots and each event added it reduces the available timeslots for that day

    def __str__(self):
        return self.day_name
    def __repr__(self):
        return self.day_name


# events need to have a date and location
class Event:
    def __init__(self, day: str, start_time: list[int], end_time: list[int], title: str, location: str):
        self.day = day
        self.location = location
        self.title = title.title()
        self.start_time = datetime(hour=start_time[0],
                                   minute=start_time[1],
                                   year=2025,
                                   day=days_of_week[self.day] + 1,
                                   month=12,
                                   second=0)
        self.end_time = datetime(hour=end_time[0],
                                 minute=end_time[1],
                                 year=2025,
                                 day=days_of_week[self.day] + 1,
                                 month=12,
                                 second=0)
        self.duration = self.end_time - self.start_time


    def __str__(self):
        return f'{self.title}, at {self.location}, on {self.day}, at {self.start_time.hour}:{self.start_time.minute}'

    def __repr__(self):
        return (f"Event: {self.title}, for {self.duration}, at {self.start_time}, till {self.end_time}, "
                f"at {self.location}, on {self.day}")

Monday = Day('monday')

week = []

for d in days_of_week.keys():
    d = Day(d)
    week.append(d)


school = Event('monday', [12, 20], [14, 30], 'School', "MSU")

Monday.add_event(school)

print(Monday.timeslots)