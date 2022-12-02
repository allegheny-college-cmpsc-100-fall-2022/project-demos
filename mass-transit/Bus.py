import os
import shutil
from pathlib import Path

class Stack:

    def __init__(self):
        # When initializing the object,
        # read the values from the file
        self.filename = "route"

    def exists(self) -> bool:
        # Check if file exists
        return os.path.exists(self.filename)
    
    def read(self) -> list:
        values = None
        # If file doesn't exist, make it
        if not self.exists():
            Path(self.filename).touch()
        # Read the file
        with open(self.filename, "r") as fh:
            values = fh.readlines()
        # Set list of values
        self.values = values
        self.length = len(self.values)
    
    def push(self, value: str = "") -> None:
        # Add value to list of values
        self.values.append(f"{value}\n")
        # Write the list
        self.write()

    def pop(self) -> str:
        value = None
        # Try to pop a value from the list
        try:
            value = self.values.pop()
        # If there are no items in the list
        # report an empty stack
        except IndexError:
            value = "STACK EMPTY"
        self.write()
        self.length = len(self.values)
        return value.strip()

    def write(self) -> None:
        # Write the list to the stack
        with open(self.filename, "w") as fh:
            for val in self.values:
                fh.write(f"{val}")

STACK = Stack()

def symlink():
    try:
        os.symlink(f"../{STACK.filename}", STACK.filename)
    except:
        pass

def report():
    cwd = os.getcwd()
    STACK.push(cwd)

def main():
    while True:
        choice = input("[F]orward or [B]ackward: ").lower()
        if choice in ["f","b"]:
            break
        print("Invalid choice.")
    if choice == "f":
        symlink()
        STACK.read()
        choice = input("Where do you want to go? ").upper()
        destination = shutil.move(f"{os.getcwd()}/Bus.py", f"{choice}/Bus.py")
        report()
    if choice == "b":
        STACK.read()
        goto = STACK.pop()
        shutil.move(f"{os.getcwd()}/Bus.py", f"{goto}/Bus.py")

if __name__ == "__main__":
    main()