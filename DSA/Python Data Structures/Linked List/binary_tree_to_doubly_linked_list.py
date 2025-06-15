# Convert Binary Tree to Doubly Linked List
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def tree_to_dll(root):
    def inorder(node):
        nonlocal last, head
        if not node:
            return
        inorder(node.left)
        new_node = DNode(node.data)
        if last:
            last.next = new_node
            new_node.prev = last
        else:
            head = new_node
        last = new_node
        inorder(node.right)
    last = None
    head = None
    inorder(root)
    return head
# Example usage omitted for brevity
