"""
865. Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, return the smallest subtree containing all the deepest nodes.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

Constraints:
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- The answer is guaranteed to be unique.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtreeWithAllDeepest(root):
    def dfs(node):
        if not node:
            return (0, None)
        l_depth, l_node = dfs(node.left)
        r_depth, r_node = dfs(node.right)
        if l_depth > r_depth:
            return (l_depth + 1, l_node)
        if r_depth > l_depth:
            return (r_depth + 1, r_node)
        return (l_depth + 1, node)
    return dfs(root)[1]

# Example usage:
# Helper function to build a tree from list
# ...omitted for brevity...
