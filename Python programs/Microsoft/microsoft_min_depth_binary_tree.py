# Microsoft: Find the minimum depth of a binary tree
def min_depth(root):
    if not root:
        return 0
    if not root.left or not root.right:
        return 1 + max(min_depth(root.left), min_depth(root.right))
    return 1 + min(min_depth(root.left), min_depth(root.right))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.left = b; a.right = c
    print("Min depth:", min_depth(a))
