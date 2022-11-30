import json

from Word import Word
from Template import Template
from Replacer import Replacer

def main():
    madlib = Template()
    word = Word()
    replaced = Replacer(madlib, word)
    print(replaced.result)
    

if __name__ == "__main__":
    main()