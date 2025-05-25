# Turing: Serialize and Deserialize Binary Tree
# Design an algorithm to serialize and deserialize a binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    vals = []
    def dfs(node):
        if node:
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        else:
            vals.append('#')
    dfs(root)
    return ' '.join(vals)

def deserialize(data):
    vals = iter(data.split())
    def dfs():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()

# Example usage and test cases can be added as needed.
