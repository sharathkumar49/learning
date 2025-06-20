"""
Longest ZigZag path in a binary tree (LeetCode 1372)
Return the length of the longest ZigZag path in a binary tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def longest_zigzag(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node, left, right):
        nonlocal res
        if not node:
            return
        res = max(res, left, right)
        dfs(node.left, right + 1, 0)
        dfs(node.right, 0, left + 1)
    dfs(root, 0, 0)
    return res
