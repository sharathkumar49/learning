# Program: Implement a Queue that supports finding the maximum in O(1)
# Problem: Design a queue that supports enqueue, dequeue, and getMax in O(1) time.

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

class MaxQueue:
    def __init__(self):
        self.q = Queue()
        self.maxq = deque()
    def enqueue(self, x):
        self.q.enqueue(x)
        while self.maxq and self.maxq[-1] < x:
            self.maxq.pop()
        self.maxq.append(x)
    def dequeue(self):
        if self.q.is_empty():
            print('Queue is empty')
            return None
        x = self.q.dequeue()
        if self.maxq and x == self.maxq[0]:
            self.maxq.popleft()
        return x
    def get_max(self):
        if not self.maxq:
            print('Queue is empty')
            return None
        return self.maxq[0]

if __name__ == '__main__':
    mq = MaxQueue()
    mq.enqueue(1)
    mq.enqueue(3)
    mq.enqueue(2)
    print(mq.get_max())
    mq.dequeue()
    print(mq.get_max())
    mq.dequeue()
    print(mq.get_max())
    mq.dequeue()
    print(mq.get_max())  # Should print empty
