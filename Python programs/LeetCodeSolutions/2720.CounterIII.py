"""
LeetCode 2720. Counter III

Implement a counter with increment, decrement, and reset methods (thread-safe).

Constraints:
- 0 <= n <= 1000
"""
import threading
class Counter:
    def __init__(self, n):
        self.init = n
        self.val = n
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.val += 1
            return self.val
    def decrement(self):
        with self.lock:
            self.val -= 1
            return self.val
    def reset(self):
        with self.lock:
            self.val = self.init
            return self.val
# Example usage:
# c = Counter(5)
# print(c.increment())  # Output: 6
# print(c.decrement())  # Output: 5
# print(c.reset())      # Output: 5
