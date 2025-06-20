# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Example:
# Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
#        [[],[-2],[0],[-3],[],[],[],[]]
# Output: [null,null,null,null,-3,null,0,-2]
#
# Constraints:
# Methods pop, top and getMin operations will always be called on non-empty stacks.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Example usage
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print("Min:", minStack.getMin())  # Output: -3
minStack.pop()
print("Top:", minStack.top())      # Output: 0
print("Min:", minStack.getMin())   # Output: -2
