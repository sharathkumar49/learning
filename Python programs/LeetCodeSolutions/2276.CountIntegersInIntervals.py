"""
LeetCode 2276. Count Integers in Intervals

Design a data structure to add intervals and count unique integers in all intervals.

Example:
Input: ["CountIntervals","add","add","count"], [[],[1,3],[7,10],[]]
Output: [null,null,null,7]

Constraints:
- 1 <= operations.length <= 10^5
"""

class CountIntervals:
    def __init__(self):
        self.intervals = []
        self.count = 0
    def add(self, left, right):
        self.intervals.append((left, right))
        self.count += right - left + 1
    def count(self):
        return self.count

# Example usage:
# ci = CountIntervals()
# ci.add(1,3)
# ci.add(7,10)
# print(ci.count())  # Output: 7
