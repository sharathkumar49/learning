# Amazon: Binary Tree Level Order Traversal
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.left = b; a.right = c
    print("Level order:", level_order(a))
