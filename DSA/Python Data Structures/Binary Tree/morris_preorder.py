"""
Morris Preorder Traversal (O(1) space)
Prints the preorder traversal of a binary tree using Morris Traversal.
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def morris_preorder(root: Optional[TreeNode]) -> List[int]:
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            if not pred.right:
                res.append(curr.val)
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                curr = curr.right
    return res
