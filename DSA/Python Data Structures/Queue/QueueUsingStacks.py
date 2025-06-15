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

class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            print('Queue is empty')
            return None
        return self.s2.pop()
    def is_empty(self):
        return not self.s1 and not self.s2

if __name__ == '__main__':
    q = QueueUsingStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
