"""
weekly schedule planner
store all events
have a set of days with repeating events as default events 
have a weekly and daily timeline
"""
from datetime import datetime
import re

time_pattern = r'^\d{1,2}:\d{1,2}$'
days_of_week = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
id_tags= []
class TimeSlotError(Exception):
    pass

class Day:
    workdays = ['tuesday', 'thursday']

    def __init__(self, day: str):
        self.day_name = day
        self.number = days_of_week[day.lower()]
        self.events = []
        self.timeslots = {x: [] for x in
                          (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)}
        if day.lower() in Day.workdays:
            shift = Event(self.day_name, "15:00", '19:00', 'Work', "Mister car wash")
            self.add_event(shift)
        if day.lower() == 'saturday':
            s = Event(self.day_name, '08:00', '17:00', 'Work', "Mister car wash")
            self.add_event(s)

    def add_event(self, event):
        if 0 == len(self.timeslots[int(event.start_time.hour)]):
            self.events.append(event)
            self.events.sort(key=lambda e: e.start_time)
            self.timeslots.update({int(event.start_time.hour): event.title})

        else:
            print("Already an Event at that timeslot")

    def remove_event(self, event):
        self.events.remove(event)
        self.timeslots.update({int(event.start_time.hour): []})
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
    def __init__(self, day: str, start_time: str, end_time: str, title: str, location: str, tags: set[str] = None):
        self.day_num = days_of_week[day.lower()]
        self.location = location
        self.day = day
        self.tags = tags
        self.title = title
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")
        self.duration = self.end_time - self.start_time

    def __str__(self):
        return f'{self.title}, at {self.location}, on {self.day}, at {self.start_time.hour}:{self.start_time.minute}'

    def __repr__(self):
        return (
            f"Event: {self.title}, for {self.duration.total_seconds() // 3600} hours, at {self.start_time}, till {self.end_time}, "
            f"at {self.location}, on {self.day}")


class User:
    #User needs to be able to have default events as well as have a week and a timeline and a schedule
    def __init__(self, name):
        self.name = name
        self.schedule = []
        self.timeslots = {x: [] for x in range((7*24))}
        self.week = [Day(x) for x in days_of_week]


    def add_default_event(self, event):
        pass

    def add_event(self, *args):
        for event in args:
            self.schedule.append(event)
            self.week[event.day_num].add_event(event)

    def __repr__(self):
        return self.name


Gareth = User('Gareth')
work = Event('wednesday', '15:00', '19:00', 'Work', "Mister car wash")
school = Event('monday', '12:20', '14:30', 'school(pmo)', 'Missouri State University')
Gareth.add_event(school, work)

def create_event():
    event_day = input("What is the day of your event? ").lower
    while event_day not in days_of_week.keys():
        event_day = input("please give a valid day of the week. What is the day of your event? ").lower()
    event_start_time = input("What is the start time of your event? ")
    while not re.fullmatch(r"^\d{1,2}:\d{1,2}$", event_start_time):
        event_start_time = input("please give a valid start time example: (14:30) ")
    event_end_time = input("What is the end time of your event? ")
    while not re.fullmatch(r"^\d{1,2}:\d{1,2}$", event_end_time):
        event_end_time = input("please give a valid end time example: (14:30) ")
    event_title = input("What is the name of your event? ")
    event_location = input("What is the location of your event? ")
    #event_tags = input("What are the tags of your event? ")
    return Event(event_day, event_start_time, event_end_time, event_title, event_location,)

new_event = create_event()
Gareth.add_event(new_event)

print(Gareth.schedule)

print()