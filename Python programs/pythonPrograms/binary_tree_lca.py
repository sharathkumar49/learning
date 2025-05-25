# Lowest common ancestor in binary tree
def lca(root, n1, n2):
    if not root:
        return None
    if root.val == n1 or root.val == n2:
        return root
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    if left and right:
        return root
    return left or right

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3); d = Node(4); e = Node(5)
    a.left = b; a.right = c; b.left = d; b.right = e
    ancestor = lca(a, 4, 5)
    print("LCA of 4 and 5:", ancestor.val if ancestor else None)
