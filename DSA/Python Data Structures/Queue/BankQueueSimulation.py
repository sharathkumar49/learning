# Program: Implement a Queue for Simulating a Bank Queue System
# Problem: Simulate a bank queue where each customer has a service time, and print the order of service.
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

def bank_queue(customers):
    q = Queue()
    for customer in customers:
        q.enqueue(customer)
    time = 0
    order = []
    while not q.is_empty():
        name, service_time = q.dequeue()
        time += service_time
        order.append((name, time))
    return order

if __name__ == '__main__':
    customers = [('Alice', 2), ('Bob', 3), ('Charlie', 1)]
    print(bank_queue(customers))
