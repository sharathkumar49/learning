# Amazon: Binary Tree Zigzag Level Order Traversal
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def zigzag_level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    left_to_right = True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right
    return res

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3); d = Node(4); e = Node(5)
    a.left = b; a.right = c; b.left = d; b.right = e
    print("Zigzag level order:", zigzag_level_order(a))
