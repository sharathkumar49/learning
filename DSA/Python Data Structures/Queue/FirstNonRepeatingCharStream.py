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
    def front(self):
        return self.buffer[-1] if not self.is_empty() else None

def first_non_repeating(stream):
    q = Queue()
    freq = {}
    result = []
    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.enqueue(ch)
        while not q.is_empty() and freq[q.front()] > 1:
            q.dequeue()
        result.append(q.front() if not q.is_empty() else '#')
    return result

if __name__ == '__main__':
    stream = "aabc"
    print(first_non_repeating(stream))
