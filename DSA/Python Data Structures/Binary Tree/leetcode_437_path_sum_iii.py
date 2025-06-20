"""
LeetCode 437: Path Sum III (Amazon, Facebook)
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def path_sum(root: Optional[TreeNode], targetSum: int) -> int:
    def dfs(node, curr_sum):
        if not node:
            return 0
        res = 0
        if node.val == curr_sum:
            res += 1
        res += dfs(node.left, curr_sum - node.val)
        res += dfs(node.right, curr_sum - node.val)
        return res
    if not root:
        return 0
    return dfs(root, targetSum) + path_sum(root.left, targetSum) + path_sum(root.right, targetSum)
