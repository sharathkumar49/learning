"""
LeetCode 617: Merge Two Binary Trees (Amazon, Facebook)
Given two binary trees, merge them into a new binary tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not t1 and not t2:
        return None
    val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
    root = TreeNode(val)
    root.left = merge_trees(t1.left if t1 else None, t2.left if t2 else None)
    root.right = merge_trees(t1.right if t1 else None, t2.right if t2 else None)
    return root
