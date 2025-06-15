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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if self.front is None:
            print('Queue is empty')
            return None
        x = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return x
    def get_front(self):
        if self.front is None:
            print('Queue is empty')
            return None
        return self.front.data
    def is_empty(self):
        return self.front is None

if __name__ == '__main__':
    q = LinkedListQueue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.dequeue())
    print(q.get_front())
    print(q.dequeue())
    print(q.dequeue())
