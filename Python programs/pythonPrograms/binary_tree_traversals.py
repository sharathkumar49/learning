# Binary tree traversals (inorder, preorder, postorder, level order)
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

def level_order(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.left = b; a.right = c
    print("Inorder:", end=' "); inorder(a); print()
    print("Preorder:", end=' "); preorder(a); print()
    print("Postorder:", end=' "); postorder(a); print()
    print("Level order:", end=' "); level_order(a); print()
