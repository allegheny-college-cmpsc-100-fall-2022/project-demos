from datetime import datetime
from Thief import Thief

def now():
    return datetime.now().timestamp()

def timeout(time):
    limit = 5
    return now() - time > limit

def load(filename):
    fh = open(filename, "r")
    return fh.readlines()

def save(books):
    fh = open("data/books.library", "w")
    for book in books:
        fh.write(f"{book}")

def main():
    books = load("data/books.library")
    thief = Thief(now())
    while True:
        attempt = input("[T]hwart the thief? ").lower()
        if timeout(thief.appears):
            print("TIMEOUT!")
            books = thief.steal(books)
        if attempt == "t":
            thief.thwart()
        if thief.complete:
            break
    save(books)

if __name__ == "__main__":
    main()