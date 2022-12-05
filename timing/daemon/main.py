import json
import random

from Tick import Tick
from time import sleep

def load(filename: str = "tickers.json") -> dict:
    with open(filename, "r") as fh:
        return json.load(fh)

def save(tickers: dict = {}, filename: str = "tickers.json") -> None:
    with open(filename, "w") as fh:
        json.dump(tickers, fh)

def cook_books() -> float:
    neg_pos = 1
    if random.random() > .5:
        neg_pos = -1
    return random.random() * neg_pos

def main():

    t = Tick(5)

    while True:
        # Loading the ticker
        tickers = load()
        print(".")
        sleep(1)
        is_elapsed = t.elapsed()
        if is_elapsed:
            # Choose one to manipulate
            chosen = random.choice(
                list(tickers.keys())
            )
            tickers[chosen]["price"] += cook_books()
            print("Save ticker")
            save(tickers)
            t = Tick(5)
            print("Load ticker")
            tickers = load()

if __name__ == "__main__":
    main()