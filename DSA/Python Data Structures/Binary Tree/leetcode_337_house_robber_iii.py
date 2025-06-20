"""
LeetCode 337: House Robber III (Amazon, Google)
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
Return the maximum amount of money the thief can rob tonight without alerting the police.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: Optional[TreeNode]) -> int:
    def helper(node):
        if not node:
            return (0, 0)
        left = helper(node.left)
        right = helper(node.right)
        rob_this = node.val + left[1] + right[1]
        not_rob_this = max(left) + max(right)
        return (rob_this, not_rob_this)
    return max(helper(root))
