# Program: Implement a Queue for Simulating a Restaurant Waiting List
# Problem: Simulate a restaurant waiting list where customers can join, leave, and be seated in order.
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
    def remove(self, val):
        self.buffer.remove(val)

class RestaurantWaitingList:
    def __init__(self):
        self.q = Queue()
    def join_waitlist(self, customer):
        self.q.enqueue(customer)
    def leave_waitlist(self, customer):
        try:
            self.q.remove(customer)
        except ValueError:
            print(f'{customer} not in waitlist')
    def seat_customer(self):
        if self.q.is_empty():
            print('No customers waiting')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    rwl = RestaurantWaitingList()
    rwl.join_waitlist('Alice')
    rwl.join_waitlist('Bob')
    rwl.join_waitlist('Charlie')
    rwl.leave_waitlist('Bob')
    while not rwl.is_empty():
        print(rwl.seat_customer())
