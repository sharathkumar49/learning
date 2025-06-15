# Program: Implement a Queue for Simulating a Printer Spooler
# Problem: Simulate a printer spooler queue where print jobs are processed in order.
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

class PrinterSpoolerQueue:
    def __init__(self):
        self.q = Queue()
    def add_job(self, job):
        self.q.enqueue(job)
    def process_job(self):
        if self.q.is_empty():
            print('No jobs in queue')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    psq = PrinterSpoolerQueue()
    psq.add_job('Doc1')
    psq.add_job('Doc2')
    psq.add_job('Doc3')
    while not psq.is_empty():
        print(psq.process_job())
