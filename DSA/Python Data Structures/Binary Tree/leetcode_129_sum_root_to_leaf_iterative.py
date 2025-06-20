"""
LeetCode 129: Sum Root to Leaf Numbers (Amazon, Google) [Iterative Version]
Given a binary tree containing digits from 0-9 only, each root-to-leaf path represents a number. Return the total sum of all root-to-leaf numbers (iterative approach).
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers_iterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    total = 0
    stack = [(root, root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right:
            total += curr_sum
        if node.right:
            stack.append((node.right, curr_sum * 10 + node.right.val))
        if node.left:
            stack.append((node.left, curr_sum * 10 + node.left.val))
    return total
