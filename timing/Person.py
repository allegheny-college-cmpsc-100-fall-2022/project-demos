from datetime import datetime

class Person:

    def __init__(self):
        self.emotion = "v. mad"
        self.last_changed = 0
    
    def change_emotion(self, emotion: str = "less mad"):
        self.last_changed = datetime.now().timestamp()
        self.emotion = emotion