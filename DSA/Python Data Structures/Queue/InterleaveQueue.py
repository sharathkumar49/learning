# Program: Implement a Queue for Interleaving the First Half of the Queue with the Second Half
# Problem: Interleave the first half of the queue with the second half using only queue operations.
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

def interleave_queue(q):
    n = q.size()
    stack = []
    for _ in range(n // 2):
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
    for _ in range(n // 2):
        q.enqueue(q.dequeue())
    for _ in range(n // 2):
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())
        q.enqueue(q.dequeue())
    return q.to_list()

if __name__ == '__main__':
    q = Queue()
    for i in [1,2,3,4,5,6]:
        q.enqueue(i)
    print(interleave_queue(q))
