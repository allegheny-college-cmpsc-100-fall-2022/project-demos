import os
import random
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
    
    def read(self) -> None:
        values = None
        # If file doesn't exist, make it
        if not self.exists():
            Path(self.filename).touch()
        # Read the file
        with open(self.filename, "r") as fh:
            values = fh.readlines()
        # Return a list of values
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

class Creature:
    def __init__(self):
	# Get location on start
        self.location = os.getcwd()
    
    def leave_trail(self, stack: Stack = Stack()):
        try:
            os.symlink(f"{self.location}/{stack.filename}", stack.filename)
        except:
            pass
        stack.read()
        stack.push(f"{self.location}")

    def record_trail(stack: Stack = Stack()):
        self.leave_trail(stack)
        self.walk()
        stack.push(self.location)
    
    def find_trail(self):
        print(self.location)
        self.next_dir = random.choice(
            [dir for dir in os.listdir(self.location) if os.path.isdir(dir)]
        )
        if self.next_dir:
            return True
        return False
    
    def walk_trail(self, destination: str = ""):
        shutil.move(f"{self.location}/Creature.py", destination)
        self.location = f"{destination}"

def main():
    # Make creature
    creature = Creature()
    # Initialize stack
    stack = Stack()
    # Get steppin'
    while creature.find_trail():
        creature.leave_trail(stack)
        creature.walk_trail(creature.next_dir)
    
        

if __name__ == "__main__":
    main()
