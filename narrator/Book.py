













import narrator
from inventory.Item import ItemSpec

class Book(ItemSpec):

    consumable = True

    def __init__(self):
        super().__init__(__file__)
        self.teller = narrator.Narrator()
        self.path = 1.0

    def __str__(self) -> str:
        return "This is the best book....ever!"

    def is_end_of_book(self,chapter_no: int = 0) -> bool:       #What chapter a
        chapters = max(self.teller.paths[int(self.path)].keys())
        if chapter_no >= chapters:
            return True
        return False

    def use(self):
        self.teller.path.change(self.path)
        while True:
            the_end = self.is_end_of_book(self.teller.path.scene)
            self.teller.narrate()
            choice = narrator.Question({
                "question": "Keep reading? ",
                "responses": [
                    {"choice": "yes", "outcome": True},
                    {"choice": "no", "outcome": False}
                ]
            })
            outcome = choice.ask()
            if not outcome or the_end:
                break

def main():
    book = Book()
    book.use()

if __name__ == "__main__":
    main()