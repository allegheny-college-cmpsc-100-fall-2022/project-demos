import json
import random

class Word:

    def __init__(self):
        fh = open("data/adjs.json","r")
        words = json.load(fh)
        self.value = random.choice(words["adjs"])
    
    def __str__(self):
        return self.value
