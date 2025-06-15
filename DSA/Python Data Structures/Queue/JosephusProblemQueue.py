# Program: Implement a Queue for Josephus Problem
# Problem: Solve the Josephus problem using a queue.
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

def josephus_problem(n, k):
    q = Queue()
    for i in range(1, n+1):
        q.enqueue(i)
    while q.size() > 1:
        for _ in range(k-1):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

if __name__ == '__main__':
    print(josephus_problem(7, 3))  # Output: 4
