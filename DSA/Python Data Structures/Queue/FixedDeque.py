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
    def enqueue_front(self, val):
        self.buffer.append(val)
    def dequeue_back(self):
        return self.buffer.popleft()

# Program: Implement a Fixed Size Double Ended Queue (Deque)
# Problem: Design a deque with fixed capacity supporting push/pop from both ends.

class FixedDeque:
    def __init__(self, k):
        self.q = Queue()
        self.capacity = k
    def is_full(self):
        return self.q.size() == self.capacity
    def is_empty(self):
        return self.q.is_empty()
    def push_front(self, x):
        if self.is_full():
            print('Deque is full')
            return False
        self.q.enqueue_front(x)
        return True
    def push_back(self, x):
        if self.is_full():
            print('Deque is full')
            return False
        self.q.enqueue(x)
        return True
    def pop_front(self):
        if self.is_empty():
            print('Deque is empty')
            return None
        return self.q.dequeue()
    def pop_back(self):
        if self.is_empty():
            print('Deque is empty')
            return None
        return self.q.dequeue_back()

if __name__ == '__main__':
    dq = FixedDeque(5)
    dq.push_back(1)
    dq.push_front(2)
    dq.push_back(3)
    print(dq.pop_front())
    print(dq.pop_back())
    print(dq.pop_front())
    print(dq.pop_front())  # Should print empty
