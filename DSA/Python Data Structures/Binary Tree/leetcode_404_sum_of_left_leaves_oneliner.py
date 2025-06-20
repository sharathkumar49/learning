"""
LeetCode 404: Sum of Left Leaves (Amazon) [One-liner Version]
Find the sum of all left leaves in a given binary tree (one-liner recursive approach).
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves_oneliner(root: Optional[TreeNode]) -> int:
    return 0 if not root else (root.left.val if root.left and not root.left.left and not root.left.right else 0) + sum_of_left_leaves_oneliner(root.left) + sum_of_left_leaves_oneliner(root.right)
