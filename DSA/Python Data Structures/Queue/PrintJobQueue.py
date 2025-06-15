# Program: Implement a Queue for Print Job Scheduling
# Problem: Simulate a print job queue with priorities.
from collections import deque
import heapq

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

class PrintJobQueue:
    def __init__(self):
        self.heap = []
        self.count = 0
    def add_job(self, job, priority):
        heapq.heappush(self.heap, (priority, self.count, job))
        self.count += 1
    def process_job(self):
        if not self.heap:
            print('No jobs in queue')
            return None
        return heapq.heappop(self.heap)[2]
    def is_empty(self):
        return not self.heap

if __name__ == '__main__':
    pq = PrintJobQueue()
    pq.add_job('Print A', 2)
    pq.add_job('Print B', 1)
    pq.add_job('Print C', 3)
    while not pq.is_empty():
        print(pq.process_job())
