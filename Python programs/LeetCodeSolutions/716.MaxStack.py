"""
LeetCode 716. Max Stack

Design a max stack that supports push, pop, top, peekMax, and popMax operations.

Implement the MaxStack class:
- MaxStack() Initializes the stack object.
- void push(int x) Pushes element x onto the stack.
- int pop() Removes the element on top of the stack and returns it.
- int top() Gets the element on the top.
- int peekMax() Retrieves the maximum element in the stack.
- int popMax() Retrieves the maximum element in the stack, and removes it. If there is more than one maximum element, only remove the top-most one.

Example 1:
Input
["MaxStack","push","push","top","popMax","top","peekMax","pop","top"]
[[],[5],[1],[],[],[],[],[],[]]
Output
[null,null,null,1,5,1,1,1,null]

Constraints:
- -10^7 <= x <= 10^7
- At most 10^4 calls will be made to push, pop, top, peekMax, and popMax.
"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])
    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def peekMax(self) -> int:
        return self.max_stack[-1]
    def popMax(self) -> int:
        max_val = self.peekMax()
        buffer = []
        while self.top() != max_val:
            buffer.append(self.pop())
        self.pop()  # remove max
        while buffer:
            self.push(buffer.pop())
        return max_val

# Example usage
if __name__ == "__main__":
    ms = MaxStack()
    ms.push(5)
    ms.push(1)
    print(ms.top())      # Output: 1
    print(ms.popMax())   # Output: 5
    print(ms.top())      # Output: 1
    print(ms.peekMax())  # Output: 1
    print(ms.pop())      # Output: 1
