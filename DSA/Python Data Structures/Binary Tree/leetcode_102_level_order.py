"""
LeetCode 102: Binary Tree Level Order Traversal (Amazon, Microsoft)
Given the root of a binary tree, return the level order traversal of its nodes' values.
"""
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
