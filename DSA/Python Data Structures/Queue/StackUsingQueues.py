from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        return self.q1.dequeue()
    def top(self):
        if self.q1.is_empty():
            return None
        return self.q1.buffer[-1]
    def empty(self):
        return self.q1.is_empty()

if __name__ == '__main__':
    s = StackUsingQueues()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # 3
    print(s.top())  # 2
