# Program: Implement a Queue for Hot Potato Game
# Problem: Simulate the Hot Potato game using a queue.
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

def hot_potato(names, num):
    q = Queue()
    for name in names:
        q.enqueue(name)
    while q.size() > 1:
        for _ in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

if __name__ == '__main__':
    names = ['A', 'B', 'C', 'D', 'E']
    print(hot_potato(names, 3))  # Output: winner
