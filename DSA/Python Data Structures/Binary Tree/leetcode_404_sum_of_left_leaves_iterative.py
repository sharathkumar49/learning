"""
LeetCode 404: Sum of Left Leaves (Amazon) [Iterative Version]
Find the sum of all left leaves in a given binary tree (iterative approach).
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves_iterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stack = [root]
    total = 0
    while stack:
        node = stack.pop()
        if node.left:
            if not node.left.left and not node.left.right:
                total += node.left.val
            else:
                stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total
