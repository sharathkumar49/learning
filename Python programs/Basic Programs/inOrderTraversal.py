

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def in_order_traversal(root):
    if root:
        # Traverse the left subtree
        in_order_traversal(root.left)
        # Visit the root
        print(root.val, end=' ')
        # Traverse the right subtree
        in_order_traversal(root.right)

# Create the tree
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(13)
root.right.left = Node(17)
root.right.right = Node(25)
root.left.left.left = Node(3)
root.left.left.right = Node(7)
root.left.right.left = Node(11)
root.left.right.right = Node(14)
root.right.left.left = Node(16)
root.right.left.right = Node(19)
root.right.right.left = Node(22)
root.right.right.right = Node(27)

# Perform in-order traversal
in_order_traversal(root)
