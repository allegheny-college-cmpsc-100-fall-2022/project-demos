from datetime import datetime

class Tick:

    def __init__(self, limit: int = 60):
        self.limit = limit
        self.start = self.now()

    def now(self):
        return datetime.now().timestamp()
    
    def elapsed(self) -> bool:
        return self.now() - self.start > self.limit