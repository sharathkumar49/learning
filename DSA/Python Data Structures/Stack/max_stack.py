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

class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()
    def push(self, val):
        self.stack.push(val)
        if self.max_stack.is_empty() or val >= self.max_stack.peek():
            self.max_stack.push(val)
    def pop(self):
        val = self.stack.pop()
        if val == self.max_stack.peek():
            self.max_stack.pop()
        return val
    def top(self):
        return self.stack.peek()
    def get_max(self):
        return self.max_stack.peek()

# Example usage
if __name__ == "__main__":
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(5)
    print(s.get_max())  # 5
    s.pop()
    print(s.get_max())  # 5
    s.pop()
    print(s.get_max())  # 5
