# 232. Implement Queue using Stacks
# Implement a first in first out (FIFO) queue using only two stacks.
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
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

# Example usage
q = MyQueue()
q.push(1)
q.push(2)
print("Peek:", q.peek())  # Output: 1
print("Pop:", q.pop())    # Output: 1
print("Empty:", q.empty()) # Output: False
