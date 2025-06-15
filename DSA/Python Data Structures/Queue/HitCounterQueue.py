from collections import deque
import time

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

class HitCounter:
    def __init__(self):
        self.q = Queue()
    def hit(self, timestamp):
        self.q.enqueue(timestamp)
    def get_hits(self, current_time, window=300):
        while not self.q.is_empty() and current_time - self.q.buffer[-1] >= window:
            self.q.dequeue()
        return self.q.size()

if __name__ == '__main__':
    hc = HitCounter()
    now = int(time.time())
    hc.hit(now-301)
    hc.hit(now-200)
    hc.hit(now-100)
    hc.hit(now)
    print(hc.get_hits(now))
