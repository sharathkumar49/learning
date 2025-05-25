# Simple rate limiter (class-based)
import time

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
    def allow(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.period]
        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False

if __name__ == "__main__":
    rl = RateLimiter(3, 5)  # 3 calls per 5 seconds
    for i in range(5):
        print("Allowed?", rl.allow())
        time.sleep(1)
