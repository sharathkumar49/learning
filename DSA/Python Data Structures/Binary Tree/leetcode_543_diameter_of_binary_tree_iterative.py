"""
LeetCode 543: Diameter of Binary Tree (Amazon, Microsoft) [Iterative Version]
Given the root of a binary tree, return the length of the diameter of the tree (iterative approach).
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree_iterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    max_diameter = 0
    node_depth = {None: 0}
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                left = node_depth[node.left]
                right = node_depth[node.right]
                node_depth[node] = 1 + max(left, right)
                max_diameter = max(max_diameter, left + right)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
    return max_diameter
