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

def spiral_level_order_traversal(root):
    if not root:
        return
    s1 = []  # Left to Right
    s2 = []  # Right to Left
    s1.append(root)
    while s1 or s2:
        while s1:
            node = s1.pop()
            print(node.data, end=' ')
            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)
        while s2:
            node = s2.pop()
            print(node.data, end=' ')
            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append(node.left)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    spiral_level_order_traversal(root)
