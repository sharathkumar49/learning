"""
LeetCode 2265. Count Nodes Equal to Sum of Descendants

Given the root of a binary tree, return the number of nodes where the value equals the sum of its descendants.

Example:
Input: root = [10,3,4,2,1]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [1, 10^5]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    res = [0]
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        if node.val == left + right:
            res[0] += 1
        return node.val + left + right
    dfs(root)
    return res[0]

# Example usage:
# root = TreeNode(10, TreeNode(3, TreeNode(2), TreeNode(1)), TreeNode(4))
# print(countNodes(root))  # Output: 2
