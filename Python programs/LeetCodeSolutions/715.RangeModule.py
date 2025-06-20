"""
LeetCode 715. Range Module

A Range Module is a module that tracks ranges of numbers. Implement the RangeModule class:
- RangeModule() Initializes the object.
- void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval.
- boolean queryRange(int left, int right) Returns true if every real number in [left, right) is currently being tracked.
- void removeRange(int left, int right) Stops tracking every real number currently being tracked in [left, right).

Example 1:
Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Constraints:
- 1 <= left < right <= 10^9
- At most 10^4 calls will be made to addRange, queryRange, and removeRange.
"""
import bisect

class RangeModule:
    def __init__(self):
        self.ranges = []
    def addRange(self, left: int, right: int) -> None:
        new = []
        placed = False
        for l, r in self.ranges:
            if r < left:
                new.append((l, r))
            elif right < l:
                if not placed:
                    new.append((left, right))
                    placed = True
                new.append((l, r))
            else:
                left = min(left, l)
                right = max(right, r)
        if not placed:
            new.append((left, right))
        self.ranges = new
    def queryRange(self, left: int, right: int) -> bool:
        for l, r in self.ranges:
            if l <= left and right <= r:
                return True
        return False
    def removeRange(self, left: int, right: int) -> None:
        new = []
        for l, r in self.ranges:
            if r <= left or l >= right:
                new.append((l, r))
            else:
                if l < left:
                    new.append((l, left))
                if r > right:
                    new.append((right, r))
        self.ranges = new

# Example usage
if __name__ == "__main__":
    rm = RangeModule()
    rm.addRange(10, 20)
    rm.removeRange(14, 16)
    print(rm.queryRange(10, 14))  # Output: True
    print(rm.queryRange(13, 15))  # Output: False
    print(rm.queryRange(16, 17))  # Output: True
