"""
Flip equivalent binary trees (LeetCode 951)
Two binary trees are flip equivalent if they are the same after some number of flip operations.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def flip_equiv(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2 or root1.val != root2.val:
        return False
    return (flip_equiv(root1.left, root2.left) and flip_equiv(root1.right, root2.right)) or \
           (flip_equiv(root1.left, root2.right) and flip_equiv(root1.right, root2.left))
