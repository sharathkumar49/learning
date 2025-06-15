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

class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()
    def _rebalance(self):
        while len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        while len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())
    def pushFront(self, val):
        self.left.appendleft(val)
        self._rebalance()
    def pushMiddle(self, val):
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)
        self._rebalance()
    def pushBack(self, val):
        self.right.append(val)
        self._rebalance()
    def popFront(self):
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._rebalance()
        return val
    def popMiddle(self):
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self._rebalance()
        return val
    def popBack(self):
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val

if __name__ == '__main__':
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushBack(2)
    q.pushMiddle(3)
    q.pushMiddle(4)
    print(q.popFront())   # 1
    print(q.popMiddle())  # 3
    print(q.popMiddle())  # 4
    print(q.popBack())    # 2
