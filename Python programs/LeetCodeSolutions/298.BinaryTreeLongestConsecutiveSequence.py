"""
298. Binary Tree Longest Consecutive Sequence

Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is a path where the values increase by 1 at each step. The path can be started at any node in the tree and must go downwards (traveling only from parent nodes to child nodes).

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent_val, length):
            if not node:
                return length
            if node.val == parent_val + 1:
                left = dfs(node.left, node.val, length + 1)
                right = dfs(node.right, node.val, length + 1)
                return max(length, left, right)
            else:
                left = dfs(node.left, node.val, 1)
                right = dfs(node.right, node.val, 1)
                return max(length, left, right)
        if not root:
            return 0
        return max(dfs(root, root.val - 1, 0), 1)

# Example usage:
# root = TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4, None, TreeNode(5))))
# print(Solution().longestConsecutive(root))  # Output: 3
