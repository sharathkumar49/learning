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

def knows(M, a, b):
    return M[a][b] == 1

def find_celebrity(M, n):
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    while q.size() > 1:
        a = q.dequeue()
        b = q.dequeue()
        if knows(M, a, b):
            q.enqueue(b)
        else:
            q.enqueue(a)
    if q.is_empty():
        return -1
    candidate = q.dequeue()
    for i in range(n):
        if i != candidate and (knows(M, candidate, i) or not knows(M, i, candidate)):
            return -1
    return candidate

if __name__ == '__main__':
    M = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    print(find_celebrity(M, 4))
