# 232. Implement Queue using Stacks (Single Stack)
# Implement a first in first out (FIFO) queue using only one stack and recursion.
#
# Example 1:
# Input: ["MyQueue","push","push","peek","pop","empty"]
#        [[],[1],[2],[],[],[]]
# Output: [null,null,null,1,1,false]
#
# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.

class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 1:
            return self.stack.pop()
        x = self.stack.pop()
        res = self.pop()
        self.stack.append(x)
        return res

    def peek(self) -> int:
        if len(self.stack) == 1:
            return self.stack[-1]
        x = self.stack.pop()
        res = self.peek()
        self.stack.append(x)
        return res

    def empty(self) -> bool:
        return not self.stack

# Example usage
q = MyQueue()
q.push(1)
q.push(2)
print("Peek:", q.peek())  # Output: 1
print("Pop:", q.pop())    # Output: 1
print("Empty:", q.empty()) # Output: False
