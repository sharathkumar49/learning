from collections import deque
from queue import Queue

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

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self, x):
        self.stack1.push(x)
    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("Queue is empty")
        return self.stack2.pop()
    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()
    def size(self):
        return self.stack1.size() + self.stack2.size()

# Example usage
if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
