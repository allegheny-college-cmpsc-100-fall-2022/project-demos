from Stack import Stack

def add(stack: Stack = Stack()):
    while True:
        value = input("Enter a value to add: ")
        if not value:
            break
        stack.push(value)

def unpack(stack: Stack = Stack()):
    return stack.pop()

def main():
    stack = Stack()
    while True:
        choice = input("[A]dd / [U]npack: ").lower()
        if choice in ["a","u"]:
            break
        print("Enter a valid choice.")
    if choice == "a":
        add(stack)
    else:
        while stack.length > 0:
            print(unpack(stack).strip())
        print(unpack(stack).strip())

if __name__ == "__main__":
    main()