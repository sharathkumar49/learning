# Program: Implement a Queue for Simulating a Theme Park Ride
# Problem: Simulate a theme park ride queue where people are grouped and served in batches.
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

class ThemeParkRideQueue:
    def __init__(self, batch_size):
        self.q = Queue()
        self.batch_size = batch_size
    def join_queue(self, person):
        self.q.enqueue(person)
    def serve_batch(self):
        batch = []
        for _ in range(self.batch_size):
            if not self.q.is_empty():
                batch.append(self.q.dequeue())
            else:
                break
        return batch
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    tprq = ThemeParkRideQueue(3)
    tprq.join_queue('Person1')
    tprq.join_queue('Person2')
    tprq.join_queue('Person3')
    tprq.join_queue('Person4')
    tprq.join_queue('Person5')
    while not tprq.is_empty():
        print(tprq.serve_batch())
