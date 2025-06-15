# Program: Implement a Queue for Simulating a Car Wash Queue
# Problem: Simulate a car wash queue where cars arrive and are washed in order.
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

class CarWashQueue:
    def __init__(self):
        self.q = Queue()
    def arrive(self, car):
        self.q.enqueue(car)
    def wash(self):
        if self.q.is_empty():
            print('No cars in queue')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    cwq = CarWashQueue()
    cwq.arrive('Car1')
    cwq.arrive('Car2')
    cwq.arrive('Car3')
    while not cwq.is_empty():
        print(cwq.wash())
