# Microsoft: Serialize and Deserialize Binary Tree
# Design an algorithm to serialize and deserialize a binary tree.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return ""
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("#")
    return ','.join(res)

def deserialize(data):
    if not data:
        return None
    vals = data.split(',')
    root = TreeNode(int(vals[0]))
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if vals[i] != "#":
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)
        i += 1
        if vals[i] != "#":
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    # Example usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    data = serialize(root)
    print(data)
    new_root = deserialize(data)
    print(serialize(new_root))
