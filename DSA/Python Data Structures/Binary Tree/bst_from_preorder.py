"""
Construct BST from Preorder Traversal
Given preorder traversal of a BST, construct the BST.
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def bst_from_preorder(preorder: List[int]) -> Optional[TreeNode]:
    idx = [0]
    def helper(lower, upper):
        if idx[0] == len(preorder):
            return None
        val = preorder[idx[0]]
        if val < lower or val > upper:
            return None
        idx[0] += 1
        node = TreeNode(val)
        node.left = helper(lower, val)
        node.right = helper(val, upper)
        return node
    return helper(float('-inf'), float('inf'))
