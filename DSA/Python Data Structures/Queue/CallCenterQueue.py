# Program: Implement a Queue for Simulating a Call Center
# Problem: Simulate a call center queue where calls are answered in order and can be escalated to the front.
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

class CallCenterQueue:
    def __init__(self):
        self.q = Queue()
    def add_call(self, call):
        self.q.enqueue(call)
    def escalate_call(self, call):
        self.q.enqueue_front(call)
    def answer_call(self):
        if self.q.is_empty():
            print('No calls in queue')
            return None
        return self.q.dequeue()
    def is_empty(self):
        return self.q.is_empty()

if __name__ == '__main__':
    ccq = CallCenterQueue()
    ccq.add_call('Call 1')
    ccq.add_call('Call 2')
    ccq.escalate_call('VIP Call')
    while not ccq.is_empty():
        print(ccq.answer_call())
