"""
LeetCode 129: Sum Root to Leaf Numbers (Amazon, Google)
Given a binary tree containing digits from 0-9 only, each root-to-leaf path represents a number. Return the total sum of all root-to-leaf numbers.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root: Optional[TreeNode]) -> int:
    def dfs(node, curr_sum):
        if not node:
            return 0
        curr_sum = curr_sum * 10 + node.val
        if not node.left and not node.right:
            return curr_sum
        return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
    return dfs(root, 0)
