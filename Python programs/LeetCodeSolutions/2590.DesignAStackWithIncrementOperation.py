"""
LeetCode 2590. Design a Stack With Increment Operation

Design a stack with increment operation.

Constraints:
- 1 <= maxSize, operations.length <= 10^5
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
# cs = CustomStack(3)
# cs.push(1)
# cs.push(2)
# print(cs.pop())  # Output: 2
# cs.push(2)
# cs.push(3)
# cs.push(4)
# cs.increment(5, 100)
# cs.increment(2, 100)
# print(cs.pop())  # Output: 103
# print(cs.pop())  # Output: 202
# print(cs.pop())  # Output: 201
