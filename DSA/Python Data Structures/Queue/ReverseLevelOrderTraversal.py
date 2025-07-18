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

def reverse_level_order_traversal(root):
    if not root:
        return
    q = Queue()
    stack = []
    q.enqueue(root)
    while not q.is_empty():
        node = q.dequeue()
        stack.append(node.data)
        if node.right:
            q.enqueue(node.right)
        if node.left:
            q.enqueue(node.left)
    while stack:
        print(stack.pop(), end=' ')

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    reverse_level_order_traversal(root)
