# Microsoft: Find the maximum depth of a binary tree
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.left = b; a.right = c
    print("Max depth:", max_depth(a))
