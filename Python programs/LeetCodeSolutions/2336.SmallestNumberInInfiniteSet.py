"""
LeetCode 2336. Smallest Number in Infinite Set

Design a data structure to support popSmallest and addBack operations.

Example:
Input: ["SmallestInfiniteSet","popSmallest","addBack"], [[],[],[2]]
Output: [null,1,null]

Constraints:
- 1 <= operations.length <= 10^5
"""

import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.h = []
        self.s = set()
        self.curr = 1
    def popSmallest(self):
        if self.h:
            x = heapq.heappop(self.h)
            self.s.remove(x)
            return x
        else:
            x = self.curr
            self.curr += 1
            return x
    def addBack(self, num):
        if num < self.curr and num not in self.s:
            heapq.heappush(self.h, num)
            self.s.add(num)

# Example usage:
# s = SmallestInfiniteSet()
# print(s.popSmallest())
# s.addBack(2)
