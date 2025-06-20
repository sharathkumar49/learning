"""
LeetCode 968: Binary Tree Cameras (Google)
Place cameras on nodes of a binary tree so that every node is monitored. Return the minimum number of cameras needed.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def min_camera_cover(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 1
        left = dfs(node.left)
        right = dfs(node.right)
        if left == 0 or right == 0:
            res += 1
            return 2
        if left == 2 or right == 2:
            return 1
        return 0
    return (dfs(root) == 0) + res
