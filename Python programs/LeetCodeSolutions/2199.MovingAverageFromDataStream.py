"""
LeetCode 2199. Moving Average From Data Stream

Design a class MovingAverage that calculates the moving average of the last size values from a data stream.

Example:
Input: ["MovingAverage","next","next","next","next"], [[3],[1],[10],[3],[5]]
Output: [null,1.0,5.5,4.66667,6.0]

Constraints:
- 1 <= size <= 1000
- -10^5 <= val <= 10^5
- At most 10^4 calls will be made to next.
"""

from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.q = deque()
        self.size = size
        self.total = 0
    def next(self, val):
        self.q.append(val)
        self.total += val
        if len(self.q) > self.size:
            self.total -= self.q.popleft()
        return self.total / len(self.q)

# Example usage:
# m = MovingAverage(3)
# print(m.next(1))  # 1.0
# print(m.next(10)) # 5.5
# print(m.next(3))  # 4.66667
# print(m.next(5))  # 6.0
