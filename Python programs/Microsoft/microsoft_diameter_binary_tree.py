# Microsoft: Find the diameter of a binary tree
def diameter_of_binary_tree(root):
    diameter = 0
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    dfs(root)
    return diameter

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3); d = Node(4); e = Node(5)
    a.left = b; a.right = c; b.left = d; b.right = e
    print("Diameter:", diameter_of_binary_tree(a))
