from logic import Event, User

def create_event():
    try:
        day = input("Day: ")
        start = input("Start time: ")
        end = input("End time: ")
        title = input("Title: ")
        location = input("Location: ")

        return Event(day, start, end, title, location)

    except Exception as e:
        print(f"Error: {e}")

def create_user():
    try:
        name = input("Name: ")

        return User(name)
    except Exception as e:
        print(f"Error: {e}")