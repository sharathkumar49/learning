"""
333. Largest BST Subtree

Given the root of a binary tree, return the size of the largest Binary Search Tree (BST) subtree in the given tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^4 <= Node.val <= 10^4
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, float('inf'), float('-inf'), True)
            l_size, l_min, l_max, l_is_bst = helper(node.left)
            r_size, r_min, r_max, r_is_bst = helper(node.right)
            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                size = l_size + r_size + 1
                return (size, min(l_min, node.val), max(r_max, node.val), True)
            return (max(l_size, r_size), 0, 0, False)
        return helper(root)[0]

# Example usage:
# root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, None, TreeNode(7)))
# print(Solution().largestBSTSubtree(root))  # Output: 3
