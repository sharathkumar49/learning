"""
LeetCode 2349. Design a Circular Deque II

Design a circular deque with insert, delete, and get operations.

Example:
Input: ["MyCircularDeque","insertFront","insertLast","getFront"], [[],[1],[2],[]]
Output: [null,true,true,1]

Constraints:
- 1 <= operations.length <= 10^5
"""

class MyCircularDeque:
    def __init__(self, k):
        self.q = []
        self.k = k
    def insertFront(self, value):
        if len(self.q) < self.k:
            self.q.insert(0, value)
            return True
        return False
    def insertLast(self, value):
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        return False
    def deleteFront(self):
        if self.q:
            self.q.pop(0)
            return True
        return False
    def deleteLast(self):
        if self.q:
            self.q.pop()
            return True
        return False
    def getFront(self):
        return self.q[0] if self.q else -1
    def getRear(self):
        return self.q[-1] if self.q else -1
    def isEmpty(self):
        return not self.q
    def isFull(self):
        return len(self.q) == self.k

# Example usage:
# dq = MyCircularDeque(3)
# print(dq.insertFront(1))
# print(dq.insertLast(2))
# print(dq.getFront())
