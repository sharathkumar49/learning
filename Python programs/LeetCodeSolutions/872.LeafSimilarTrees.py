"""
872. Leaf-Similar Trees

Given the roots of two binary trees, return true if their leaf value sequence is the same.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Constraints:
- The number of nodes in each tree is in the range [1, 200].
- 0 <= Node.val <= 200
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1, root2):
    def dfs(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return dfs(node.left) + dfs(node.right)
    return dfs(root1) == dfs(root2)

# Example usage:
# Helper function to build a tree from list
# ...omitted for brevity...
