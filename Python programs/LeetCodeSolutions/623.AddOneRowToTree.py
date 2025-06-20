"""
623. Add One Row to Tree
Difficulty: Medium

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth.

Example 1:
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
The depth of the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root, val, depth):
    if depth == 1:
        return TreeNode(val, root)
    def dfs(node, d):
        if not node:
            return
        if d == depth - 1:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
        else:
            dfs(node.left, d+1)
            dfs(node.right, d+1)
    dfs(root, 1)
    return root

# Example usage
# (See LeetCode for binary tree construction examples)
