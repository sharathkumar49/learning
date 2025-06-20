"""
LeetCode 99: Recover Binary Search Tree (Two nodes swapped)
Recover the tree without changing its structure.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def recover_bst(root: Optional[TreeNode]) -> None:
    x = y = pred = prev = None
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev and curr.val < prev.val:
            y = curr
            if not x:
                x = prev
            else:
                break
        prev = curr
        curr = curr.right
    if x and y:
        x.val, y.val = y.val, x.val
