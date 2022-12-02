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

    while True:
        choice = input("[A]dd a fruit / [S]earch fruits: ").lower()
        if choice in ["a", "s"]:
            break
        print("Not valid choice!")

    if choice == "a":
        # Add data to file
        name = input("Fruit to add: ")
        price = input("Price of fruit: ")
        qty = input("Quantity we have: ")

        fruits[name.lower()] = {"price": price, "quantity": qty}

        # Write to file
        save(fruits, "fruits.json")
    
    if choice == "s":
        search = input("Fruit to search for: ").lower()
        if search in fruits:
            price = fruits[search]["price"]
            number = fruits[search]["quantity"]
            print(f"We found {search}. There are {number}. They are ${price}")
        else:
            print(f"We found no {search}.")


if __name__ == "__main__":
    main()
