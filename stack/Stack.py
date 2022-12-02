import os
from pathlib import Path

class Stack:

    def __init__(self):
        self.values = self.read()

    def exists(self) -> bool:
        return os.path.exists("stack")
    
    def read(self) -> list:
        values = None
        if not self.exists():
            Path("stack").touch()
        with open("stack", "r") as fh:
            values = fh.readlines()
        return values
    
    def push(self, value: str = "") -> None:
        self.values.append(f"{value}\n")
        self.write()

    def pop(self) -> str:
        value = None
        try:
            value = self.values.pop()
        except IndexError:
            value = "STACK EMPTY"
        self.write()
        return value

    def write(self) -> None:
        with open("stack", "w+") as fh:
            for val in self.values:
                fh.write(f"{val}")