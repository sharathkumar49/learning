"""
341. Flatten Nested List Iterator

You are given a nested list of integers nestedList. Implement an iterator to flatten it.

Constraints:
- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range [-10^6, 10^6].
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

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = []
        self._pushList(nestedList)
    def _pushList(self, nestedList):
        for ni in reversed(nestedList):
            self.stack.append(ni)
    def next(self) -> int:
        return self.stack.pop().getInteger()
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self._pushList(top.getList())
        return False

# Example usage:
# ni1 = NestedInteger(1)
# ni2 = NestedInteger([NestedInteger(2), NestedInteger(3)])
# nestedList = [ni1, ni2]
# i = NestedIterator(nestedList)
# while i.hasNext():
#     print(i.next())
