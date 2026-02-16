from logic import *
import pytest
import datetime

def test_event_init():
    e = Event(
        "Monday",
        "11:00",
        "12:15",
        "class",
        "missouri state"
    )
    assert e.day == "Monday"
    assert e.start_time == datetime.datetime(1900, 1, 1, 11, 0)
    assert e.end_time == datetime.datetime(1900, 1, 1, 12, 15)
    assert e.title == "class"
    assert e.location == "missouri state"
    assert e.duration == e.end_time - e.start_time


def test_event_parse_time():
    # Test to make sure start and end times entered with an invalid format raises an error
    with pytest.raises(ValueError):
        Event(
            "Monday",
            "-10:00",
            "20:00",
            "class",
            "missouri state"
        )
    with pytest.raises(ValueError):
        Event(
            "Monday",
            "11:00",
            "30:00",
            "class",
            "missouri state"
        )
    with pytest.raises(ValueError):
        Event(
            "Monday",
            "11:00",
            "invalid",
            "class",
            "missouri state"
        )


def test_event_valid_duration_raises():
    # Test to make sure new events raise errors when given start and end times that don't work
    with pytest.raises(TimeConflict):
        # Starts after it ends
        Event(
            "Monday",
            "11:00",
            "10:10",
            "class",
            "missouri state"
        )
    with pytest.raises(TimeConflict):
        # Starts and ends at the same time
        Event(
            "Monday",
            "11:00",
            "11:00",
            "class",
            "missouri state"
        )


def test_day_init():
    d = Day("tuesday")
    assert d.day_name == "tuesday"
    with pytest.raises(IndexError):
        Day("Hello world!")


def test_day_has_conflict():
    d = Day("monday")
    # e is the control event
    e = Event(
            "Monday",
            "11:00",
            "12:00",
            "class",
            "missouri state"
        )
    # e2 is an event that starts while the control event is going
    e2 = Event(
        "monday",
        "11:30",
        "12:30",
        "gym",
        "gym"
    )
    # e3 is the event that ends after the control event starts
    e3 = Event(
        "monday",
        "10:00",
        "11:45",
        "class",
        "school"
    )
    # e4 is the event that starts and ends during the duration of the control event
    e4 = Event(
        "monday",
        "11:15",
        "11:45",
        "title",
        "place"
    )
    d.add_event(e)
    with pytest.raises(TimeConflict):
        d.add_event(e2)
    with pytest.raises(TimeConflict):
        d.add_event(e3)
    with pytest.raises(TimeConflict):
        d.add_event(e4)

def test_day_remove_event_raises():
    e = Event(
        "monday",
        "11:15",
        "11:45",
        "title",
        "place"
    )
    e2 = Event(
        "monday",
        "11:15",
        "11:45",
        "title",
        "place"
    )
    d = Day("monday")
    with pytest.raises(IndexError):
        d.remove_event(e)
    d.add_event(e)
    with pytest.raises(KeyError):
        d.remove_event(e2)
