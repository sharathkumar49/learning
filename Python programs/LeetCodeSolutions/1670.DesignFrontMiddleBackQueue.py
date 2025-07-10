"""
LeetCode 1670. Design Front Middle Back Queue

Design a queue that supports pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack operations.

Example 1:
Input: ["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"], [[],[1],[2],[3],[4],[],[],[],[],[]]
Output: [null,null,null,null,null,1,3,4,2,-1]

Constraints:
- 1 <= operations.length <= 1000
- 1 <= val <= 10^9
"""

from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()
    def balance(self):
        while len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        while len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())
    def pushFront(self, val):
        self.left.appendleft(val)
        self.balance()
    def pushMiddle(self, val):
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)
        self.balance()
    def pushBack(self, val):
        self.right.append(val)
        self.balance()
    def popFront(self):
        if not self.left and not self.right:
            return -1
        if self.left:
            res = self.left.popleft()
        else:
            res = self.right.popleft()
        self.balance()
        return res
    def popMiddle(self):
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            res = self.left.pop()
        else:
            res = self.right.popleft()
        self.balance()
        return res
    def popBack(self):
        if not self.left and not self.right:
            return -1
        if self.right:
            res = self.right.pop()
        else:
            res = self.left.pop()
        self.balance()
        return res

# Example usage:
# q = FrontMiddleBackQueue()
# q.pushFront(1)
# q.pushBack(2)
# q.pushMiddle(3)
# q.pushMiddle(4)
# print(q.popFront())   # Output: 1
# print(q.popMiddle())  # Output: 3
# print(q.popMiddle())  # Output: 4
# print(q.popBack())    # Output: 2
# print(q.popFront())   # Output: -1
