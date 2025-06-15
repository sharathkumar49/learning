from collections import deque

# Wrapper class for queue using deque from collections
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

# Program: Implement a Circular Buffer (Ring Buffer) using Queue
# Problem: Design a circular buffer with fixed capacity supporting enqueue and dequeue.

class CircularBuffer:
    def __init__(self, k):
        self.q = Queue()
        self.capacity = k
    def enqueue(self, x):
        if self.q.size() == self.capacity:
            print('Buffer is full')
            return False
        self.q.enqueue(x)
        return True
    def dequeue(self):
        if self.q.is_empty():
            print('Buffer is empty')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()
    def is_full(self):
        return self.q.size() == self.capacity

if __name__ == '__main__':
    cb = CircularBuffer(3)
    print(cb.enqueue(1))
    print(cb.enqueue(2))
    print(cb.enqueue(3))
    print(cb.enqueue(4))  # Should print full
    print(cb.dequeue())
    print(cb.enqueue(4))
    print(cb.dequeue())
    print(cb.dequeue())
    print(cb.dequeue())
    print(cb.dequeue())  # Should print empty
