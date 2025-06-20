"""
Construct BST from Postorder Traversal
Given postorder traversal of a BST, construct the BST.
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def bst_from_postorder(postorder: List[int]) -> Optional[TreeNode]:
    idx = [len(postorder) - 1]
    def helper(lower, upper):
        if idx[0] < 0:
            return None
        val = postorder[idx[0]]
        if val < lower or val > upper:
            return None
        idx[0] -= 1
        node = TreeNode(val)
        node.right = helper(val, upper)
        node.left = helper(lower, val)
        return node
    return helper(float('-inf'), float('inf'))
