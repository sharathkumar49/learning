"""
LeetCode 124: Binary Tree Maximum Path Sum (Amazon, Microsoft) [Iterative Version]
Find the path with the maximum sum in a binary tree (iterative approach).
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum_iterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    max_sum = float('-inf')
    stack = [(root, False)]
    node_to_max = {}
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                left = max(node_to_max.get(node.left, 0), 0)
                right = max(node_to_max.get(node.right, 0), 0)
                max_sum = max(max_sum, node.val + left + right)
                node_to_max[node] = node.val + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
    return max_sum
