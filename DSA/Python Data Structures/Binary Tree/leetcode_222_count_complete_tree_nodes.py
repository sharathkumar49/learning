"""
LeetCode 222: Count Complete Tree Nodes (Google, Amazon)
Given the root of a complete binary tree, return the number of the nodes in the tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left, right = root, root
    lh = rh = 0
    while left:
        lh += 1
        left = left.left
    while right:
        rh += 1
        right = right.right
    if lh == rh:
        return (1 << lh) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)
