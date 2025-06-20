"""
LeetCode 404: Sum of Left Leaves (Amazon)
Find the sum of all left leaves in a given binary tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    total = 0
    if root.left:
        if not root.left.left and not root.left.right:
            total += root.left.val
        else:
            total += sum_of_left_leaves(root.left)
    total += sum_of_left_leaves(root.right)
    return total
