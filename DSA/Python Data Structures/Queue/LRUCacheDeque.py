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
    def to_list(self):
        return list(self.buffer)

class LRUCache:
    def __init__(self, capacity):
        self.cache = Queue()
        self.set = set()
        self.capacity = capacity
    def refer(self, x):
        if x not in self.set:
            if self.cache.size() == self.capacity:
                last = self.cache.dequeue()
                self.set.remove(last)
        else:
            self.cache.remove(x)
        self.cache.enqueue(x)
        self.set.add(x)
    def display(self):
        return self.cache.to_list()

if __name__ == '__main__':
    lru = LRUCache(4)
    lru.refer(1)
    lru.refer(2)
    lru.refer(3)
    lru.refer(1)
    lru.refer(4)
    lru.refer(5)
    print(lru.display())
