"""
LeetCode 1381. Design a Stack With Increment Operation

Design a stack which supports the following operations:
- push(x): Push element x onto stack.
- pop(): Pop and return the top of stack. If empty, return -1.
- increment(k, val): Increment the bottom k elements by val. If there are less than k elements, increment all of them.

Constraints:
- 1 <= maxSize <= 1000
- 1 <= x <= 1000
- 1 <= k <= 1000
- 0 <= val <= 100

Example:
Input: ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"], [[3], [1], [2], [], [2], [3], [4], [5,100], [2,100], [], [], [], []]
Output: [null,null,null,2,null,null,null,null,null,103,202,201,-1]
"""
class CustomStack:
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
    def pop(self):
        return self.stack.pop() if self.stack else -1
    def increment(self, k, val):
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

# Example usage:
cs = CustomStack(3)
cs.push(1)
cs.push(2)
print(cs.pop())  # 2
cs.push(2)
cs.push(3)
cs.push(4)
cs.increment(5, 100)
cs.increment(2, 100)
print(cs.pop())  # 103
print(cs.pop())  # 202
print(cs.pop())  # 201
print(cs.pop())  # -1
