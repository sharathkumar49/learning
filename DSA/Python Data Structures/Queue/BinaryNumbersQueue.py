# Program: Implement a Queue for Binary Numbers from 1 to n
# Problem: Print binary numbers from 1 to n using a queue.
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

def generate_binary_numbers(n):
    q = Queue()
    q.enqueue('1')
    result = []
    for _ in range(n):
        front = q.dequeue()
        result.append(front)
        q.enqueue(front + '0')
        q.enqueue(front + '1')
    return result

if __name__ == '__main__':
    print(generate_binary_numbers(10))
