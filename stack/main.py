from Stack import Stack

def main():
    # Make the stack object
    stack = Stack()
    
    # Get the operation user wants
    while True:
        choice = input("[A]dd / [U]npack: ").lower()
        if choice in ["a","u"]:
            break
        print("Enter a valid choice.")
    
    # Handle that choice
    if choice == "a":
        while True:
            value = input("Enter a value to add: ")
            if not value:
                break
            # Add to stack
            stack.push(value)
    else:
        while stack.length > 0:
            # Pop the LIFO value off stack
            print(stack.pop())
        print(stack.pop())

if __name__ == "__main__":
    main()