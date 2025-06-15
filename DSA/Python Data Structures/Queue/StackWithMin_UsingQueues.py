# Program: Implement a Stack with getMin() in O(1) using two Queues
# Problem: Design a stack that supports push, pop, and getMin in O(1) time using two queues.

from collections import deque

class MinStackWithQueues:
    def __init__(self):
        self.q = deque()
        self.minq = deque()
    def push(self, x):
        self.q.appendleft(x)
        if not self.minq or x <= self.minq[0]:
            self.minq.appendleft(x)
    def pop(self):
        if not self.q:
            print('Stack is empty')
            return None
        x = self.q.popleft()
        if x == self.minq[0]:
            self.minq.popleft()
        return x
    def get_min(self):
        if not self.minq:
            print('Stack is empty')
            return None
        return self.minq[0]

if __name__ == '__main__':
    s = MinStackWithQueues()
    s.push(3)
    s.push(5)
    print(s.get_min())
    s.push(2)
    s.push(1)
    print(s.get_min())
    print(s.pop())
    print(s.get_min())
    print(s.pop())
    print(s.get_min())
