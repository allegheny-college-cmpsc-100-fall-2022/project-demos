import json

def load(filename: str = "") -> dict:
    fh = open("fruits.json", "r")
    return json.load(fh)

def save(fruits: dict = {}, filename: str = "") -> None:
    fh = open("fruits.json", "w")
    json.dump(fruits, fh, indent = 4)

def main():
    # Load file on program start
    fruits = load("fruits.json")

    # Add data to file
    name = input("Fruit to add: ")
    price = input("Price of fruit: ")

    fruits[name] = price

    # Write to file
    save(fruits, "fruits.json")

if __name__ == "__main__":
    main()
