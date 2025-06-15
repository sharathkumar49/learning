from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

def min_stack():
    class MinStack:
        def __init__(self):
            self.stack = Stack()
            self.min_stack = Stack()
        def push(self, val):
            self.stack.push(val)
            if self.min_stack.is_empty() or val <= self.min_stack.peek():
                self.min_stack.push(val)
        def pop(self):
            if self.stack.pop() == self.min_stack.peek():
                self.min_stack.pop()
        def top(self):
            return self.stack.peek()
        def get_min(self):
            return self.min_stack.peek()
    return MinStack()

# Example usage
if __name__ == "__main__":
    s = min_stack()
    s.push(5)
    s.push(3)
    s.push(7)
    print(s.get_min())  # 3
    s.pop()
    print(s.get_min())  # 3
