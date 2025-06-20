"""
LeetCode 617: Merge Two Binary Trees (Amazon, Facebook) [Iterative Version]
Given two binary trees, merge them into a new binary tree (iterative approach).
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees_iterative(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not t1:
        return t2
    if not t2:
        return t1
    root = TreeNode(t1.val + t2.val)
    queue = deque([(root, t1, t2)])
    while queue:
        node, n1, n2 = queue.popleft()
        for child, c1, c2 in (("left", n1.left, n2.left), ("right", n1.right, n2.right)):
            if c1 or c2:
                if c1 and c2:
                    new_node = TreeNode(c1.val + c2.val)
                    setattr(node, child, new_node)
                    queue.append((new_node, c1, c2))
                else:
                    setattr(node, child, c1 or c2)
    return root
