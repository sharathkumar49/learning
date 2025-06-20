"""
LeetCode 199: Binary Tree Right Side View (Amazon, Facebook) [DFS Version]
Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom (DFS approach).
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view_dfs(root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(res):
            res.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    dfs(root, 0)
    return res
