# Program: Implement a Queue for Reversing the First k Elements of a Queue
# Problem: Reverse the first k elements of a queue using only queue operations.
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
    def to_list(self):
        return list(reversed(self.buffer))

def reverse_k_elements(q, k):
    stack = []
    for _ in range(k):
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
    for _ in range(q.size() - k):
        q.enqueue(q.dequeue())
    return q.to_list()

if __name__ == '__main__':
    q = Queue()
    for i in [1,2,3,4,5]:
        q.enqueue(i)
    print(reverse_k_elements(q, 3))
