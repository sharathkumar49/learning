# Implement a stack using two queues
from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        if self.q1:
            return self.q1.popleft()
        return None
    def top(self):
        return self.q1[0] if self.q1 else None
    def empty(self):
        return not self.q1

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.top())  # 2
    s.pop()
    print(s.top())  # 1
