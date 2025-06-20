"""
Print boundary of binary tree (anti-clockwise)
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def boundary_of_binary_tree(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = [root.val]
    def left_boundary(node):
        while node:
            if node.left or node.right:
                res.append(node.val)
            node = node.left if node.left else node.right
    def right_boundary(node):
        tmp = []
        while node:
            if node.left or node.right:
                tmp.append(node.val)
            node = node.right if node.right else node.left
        res.extend(tmp[::-1])
    def leaves(node):
        if node:
            leaves(node.left)
            if node != root and not node.left and not node.right:
                res.append(node.val)
            leaves(node.right)
    left_boundary(root.left)
    leaves(root)
    right_boundary(root.right)
    return res
