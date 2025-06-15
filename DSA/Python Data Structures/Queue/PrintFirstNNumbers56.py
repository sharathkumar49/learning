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

def print_first_n_numbers_56(n):
    q = Queue()
    q.enqueue('5')
    q.enqueue('6')
    result = []
    for _ in range(n):
        curr = q.dequeue()
        result.append(curr)
        q.enqueue(curr + '5')
        q.enqueue(curr + '6')
    return result

if __name__ == '__main__':
    print(print_first_n_numbers_56(10))
