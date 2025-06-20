"""
339. Nested List Weight Sum

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Return the sum of each integer in the list multiplied by its depth.

Constraints:
- 1 <= nestedList.length <= 50
- The values of the integers in the nested list is in the range [-100, 100].
"""
from typing import List, Union

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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nlist, depth):
            total = 0
            for ni in nlist:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)

# Example usage:
# ni1 = NestedInteger(1)
# ni2 = NestedInteger(1)
# ni3 = NestedInteger()
# ni3.list = [ni1, ni2]
# ni4 = NestedInteger(2)
# nestedList = [ni3, ni4]
# print(Solution().depthSum(nestedList))  # Output: 4
