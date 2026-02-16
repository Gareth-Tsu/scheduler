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

