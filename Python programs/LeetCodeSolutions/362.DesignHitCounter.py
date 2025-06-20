"""
362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Implement the HitCounter class:
- HitCounter() Initializes the object of the hit counter system.
- void hit(int timestamp) Records a hit that happened at timestamp (in seconds).
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp.

Constraints:
- 1 <= timestamp <= 2 * 10^9
- At most 300 calls will be made to hit and getHits.
"""
from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)

# Example usage:
hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
print(hc.getHits(4))    # Output: 3
hc.hit(300)
print(hc.getHits(300))  # Output: 4
print(hc.getHits(301))  # Output: 3
