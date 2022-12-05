import json

def load(filename: str = "tickers.json") -> dict:
    with open("tickers.json", "r") as fh:
        return json.load(fh)

def main():
    tickers = load()
    while True:
        choice = input("Check price: ")
        if choice not in tickers:
            print("Not valid.")
        else: break
    print(tickers[choice])

if __name__ == "__main__":
    main()