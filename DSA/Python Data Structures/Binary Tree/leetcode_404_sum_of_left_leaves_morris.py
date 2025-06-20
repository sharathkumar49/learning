"""
LeetCode 404: Sum of Left Leaves (Amazon) [Morris Traversal Version]
Find the sum of all left leaves in a given binary tree using Morris Traversal (O(1) space).
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves_morris(root: Optional[TreeNode]) -> int:
    total = 0
    curr = root
    while curr:
        if curr.left:
            pred = curr.left
            is_left_leaf = not pred.left and not pred.right
            while pred.right and pred.right != curr:
                pred = pred.right
            if not pred.right:
                if is_left_leaf:
                    total += pred.val
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                curr = curr.right
        else:
            curr = curr.right
    return total
