"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/

You have a RecentCounter class which counts the number of recent requests within a certain time window.
Implement the RecentCounter class:
- RecentCounter() Initializes the counter with zero recent requests.
- int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).

Constraints:
- 1 <= t <= 10^9
- Each test case will call ping with strictly increasing values of t.
- At most 10^4 calls will be made to ping.

Example:
Input: ["RecentCounter","ping","ping","ping","ping"], [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
"""
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Example usage
if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))    # Output: 1
    print(rc.ping(100))  # Output: 2
    print(rc.ping(3001)) # Output: 3
    print(rc.ping(3002)) # Output: 3
