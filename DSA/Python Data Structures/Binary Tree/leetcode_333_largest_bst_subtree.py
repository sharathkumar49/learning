"""
LeetCode 333: Largest BST Subtree (Google)
Given a binary tree, find the largest subtree which is a BST, and return the size of that subtree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def largest_bst_subtree(root: Optional[TreeNode]) -> int:
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
