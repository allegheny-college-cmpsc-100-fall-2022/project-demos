import os
from pathlib import Path

class Stack:

    def __init__(self):
        # When initializing the object,
        # read the values from the file
        self.values = self.read()
        self.length = len(self.values)

    def exists(self) -> bool:
        # Check if file exists
        return os.path.exists("stack")
    
    def read(self) -> list:
        values = None
        # If file doesn't exist, make it
        if not self.exists():
            Path("stack").touch()
        # Read the file
        with open("stack", "r") as fh:
            values = fh.readlines()
        # Return a list of values
        return values
    
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
        return value

    def write(self) -> None:
        # Write the list to the stack
        with open("stack", "w") as fh:
            for val in self.values:
                fh.write(f"{val}")