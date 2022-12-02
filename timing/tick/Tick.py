from datetime import datetime

class Tick:

    def now(self):
        return datetime.now().timestamp()
    
    def elapsed(self, time: float = 0, limit: int = 60) -> bool:
        return self.now() - time > limit