from Person import Person
from datetime import datetime

def time_window(person):
    now = datetime.now().timestamp()
    return now - person.last_changed

def main():
    person = Person()
    person.change_emotion()
    while time_window(person) < 5:
        print(person.emotion)
    person.change_emotion("v. mad")
    print(person.emotion)

if __name__ == "__main__":
    main()