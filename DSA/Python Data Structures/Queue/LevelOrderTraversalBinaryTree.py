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
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        node = q.dequeue()
        print(node.data, end=' ')
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    level_order_traversal(root)
