"""
Distribute coins in binary tree (LeetCode 979)
Return the minimum number of moves required to make every node have exactly one coin.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def distribute_coins(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        res += abs(left) + abs(right)
        return node.val + left + right - 1
    dfs(root)
    return res
