"""
LeetCode 2665. Counter II

Implement a counter with increment, decrement, and reset methods.

Constraints:
- 0 <= n <= 1000
"""
class Counter:
    def __init__(self, n):
        self.init = n
        self.val = n
    def increment(self):
        self.val += 1
        return self.val
    def decrement(self):
        self.val -= 1
        return self.val
    def reset(self):
        self.val = self.init
        return self.val
# Example usage:
# c = Counter(5)
# print(c.increment())  # Output: 6
# print(c.decrement())  # Output: 5
# print(c.reset())      # Output: 5
