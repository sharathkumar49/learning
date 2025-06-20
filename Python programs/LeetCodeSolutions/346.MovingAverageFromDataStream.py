"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Constraints:
- 1 <= size <= 10^4
- -10^5 <= val <= 10^5
- At most 10^4 calls will be made to next.
"""
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0
    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)

# Example usage:
m = MovingAverage(3)
print(m.next(1))  # Output: 1.0
print(m.next(10)) # Output: 5.5
print(m.next(3))  # Output: 4.666...
print(m.next(5))  # Output: 6.0
