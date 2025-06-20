"""
Count number of uni-value subtrees (LeetCode 250)
A uni-value subtree means all nodes of the subtree have the same value.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root: Optional[TreeNode]) -> int:
    count = [0]
    def is_unival(node):
        if not node:
            return True
        left = is_unival(node.left)
        right = is_unival(node.right)
        if left and right:
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            count[0] += 1
            return True
        return False
    is_unival(root)
    return count[0]
