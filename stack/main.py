from Stack import Stack

def main():
    stack = Stack()
    while True:
        choice = input("[A]dd / [U]npack: ").lower()
        if choice in ["a","u"]:
            break
        print("Enter a valid choice.")
    
    if choice == "a":
        while True:
            value = input("Enter a value to add: ")
            if not value:
                break
            stack.push(value)
    else:
        while stack.length > 0:
            print(stack.pop())
        print(stack.pop())

if __name__ == "__main__":
    main()