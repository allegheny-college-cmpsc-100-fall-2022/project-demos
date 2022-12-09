import random

class Thief:

    def __init__(self, appears):
        self.thwarted = False
        self.appears = appears
        self.complete = False
        print("The thief appears!")
    
    def thwart(self):
        self.thwarted = True
        self.complete = True
        print("The thief is thwarted!")
    
    def steal(self, books):
        self.book = random.choice(books)
        self.complete = True
        if not self.thwarted:
            books.remove(self.book)
            print("The thief steals!")
            self.save()
        return books

    def save(self):
        fh = open("data/books.stolen", "w")
        fh.write(f"{self.book}\n")