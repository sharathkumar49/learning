"""
364. Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth. The weight is defined as the inverse of the depth (i.e., the deepest level has weight 1, the level above it has weight 2, and so on).

Constraints:
- 1 <= nestedList.length <= 50
- The values of the integers in the nested list is in the range [-100, 100].
"""
from typing import List

class NestedInteger:
    def __init__(self, value=None):
        self.value = value
        self.list = []
    def isInteger(self):
        return self.value is not None
    def getInteger(self):
        return self.value
    def getList(self):
        return self.list

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        level = nestedList
        res = 0
        weighted = 0
        while level:
            next_level = []
            for ni in level:
                if ni.isInteger():
                    weighted += ni.getInteger()
                else:
                    next_level.extend(ni.getList())
            res += weighted
            level = next_level
        return res

# Example usage:
# ni1 = NestedInteger(1)
# ni2 = NestedInteger(1)
# ni3 = NestedInteger([ni1, ni2])
# ni4 = NestedInteger(2)
# nestedList = [ni3, ni4]
# print(Solution().depthSumInverse(nestedList))  # Output: 8
