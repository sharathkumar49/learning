# Program: Implement a Queue for Simulating a Ticket Counter
# Problem: Simulate a ticket counter queue where people can join the front or back of the queue.
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

class TicketCounterQueue:
    def __init__(self):
        self.q = Queue()
    def join_back(self, person):
        self.q.enqueue(person)
    def join_front(self, person):
        self.q.enqueue_front(person)
    def serve(self):
        if self.q.is_empty():
            print('No one in queue')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    tcq = TicketCounterQueue()
    tcq.join_back('Person 1')
    tcq.join_back('Person 2')
    tcq.join_front('VIP')
    while not tcq.is_empty():
        print(tcq.serve())
