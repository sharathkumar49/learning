"""
352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:
- SummaryRanges() Initializes the object with an empty data stream.
- void addNum(int value) Adds the integer value to the data stream.
- int[][] getIntervals() Returns a summary of the numbers in the data stream as a list of disjoint intervals [start, end].

Constraints:
- 0 <= value <= 10^4
- At most 3 * 10^4 calls will be made to addNum and getIntervals.
"""
from typing import List

class SummaryRanges:
    def __init__(self):
        self.nums = set()
    def addNum(self, value: int) -> None:
        self.nums.add(value)
    def getIntervals(self) -> List[List[int]]:
        arr = sorted(self.nums)
        res = []
        for num in arr:
            if not res or num > res[-1][1] + 1:
                res.append([num, num])
            else:
                res[-1][1] = num
        return res

# Example usage:
sr = SummaryRanges()
sr.addNum(1)
sr.addNum(3)
sr.addNum(7)
sr.addNum(2)
sr.addNum(6)
print(sr.getIntervals())  # Output: [[1,3],[6,7]]
