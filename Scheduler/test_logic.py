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


def test_has_conflict_returns_conflicting_event():
    d = Day("monday")
    e1 = Event("monday", "11:00", "12:00", "Existing", "loc", priority=2)
    e2 = Event("monday", "11:30", "12:30", "New", "loc", priority=3)
    d.add_event(e1)

    conflict = d.has_conflict(e2)
    # has_conflict should return the actual conflicting Event object (truthy)
    assert conflict is e1
    assert bool(conflict) is True


def test_timeconflict_exception_contains_events_and_message():
    d = Day("monday")
    # existing event has higher priority (lower number)
    existing = Event("monday", "09:00", "10:00", "ExistingH", "loc", priority=1)
    new = Event("monday", "09:30", "10:30", "NewL", "loc", priority=2)
    d.add_event(existing)

    with pytest.raises(TimeConflict) as excinfo:
        d.add_event(new)

    exc = excinfo.value
    # Exception should carry references to both events
    assert exc.existing_event is existing
    assert exc.new_event is new
    # Message should include both priorities
    assert "priority=2" in exc.message
    assert "priority=1" in exc.message


def test_add_event_replaces_lower_priority():
    d = Day("monday")
    low = Event("monday", "13:00", "14:00", "Low", "loc", priority=4)
    high = Event("monday", "13:15", "13:45", "High", "loc", priority=1)
    d.add_event(low)

    # Adding a higher-priority event that conflicts should replace the existing one
    d.add_event(high)
    assert low not in d.events
    assert high in d.events
    assert len(d.events) == 1


def test_equal_priority_raises_conflict_and_contains_events():
    d = Day("monday")
    a = Event("monday", "15:00", "16:00", "A", "loc", priority=2)
    b = Event("monday", "15:30", "16:30", "B", "loc", priority=2)
    d.add_event(a)

    with pytest.raises(TimeConflict) as excinfo:
        d.add_event(b)

    exc = excinfo.value
    assert exc.existing_event is a
    assert exc.new_event is b


def test_invalid_duration_timeconflict_has_no_events():
    # Creating an event with invalid duration raises a generic TimeConflict
    with pytest.raises(TimeConflict) as excinfo:
        Event("monday", "11:00", "11:00", "Invalid", "loc")

    exc = excinfo.value
    assert exc.new_event is None
    assert exc.existing_event is None
