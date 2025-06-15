# Program: Implement a Queue for Simulating a Supermarket Checkout
# Problem: Simulate a supermarket checkout queue where customers are served in order.
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

class SupermarketCheckoutQueue:
    def __init__(self):
        self.q = Queue()
    def join_queue(self, customer):
        self.q.enqueue(customer)
    def checkout(self):
        if self.q.is_empty():
            print('No customers in queue')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    smq = SupermarketCheckoutQueue()
    smq.join_queue('Customer1')
    smq.join_queue('Customer2')
    smq.join_queue('Customer3')
    while not smq.is_empty():
        print(smq.checkout())
