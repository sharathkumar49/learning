"""
LeetCode 987: Vertical Order Traversal of a Binary Tree (Amazon, Facebook)
Given the root of a binary tree, return the vertical order traversal of its nodes' values.
"""
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def vertical_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    node_list = []
    queue = deque([(root, 0, 0)])
    while queue:
        node, x, y = queue.popleft()
        node_list.append((x, y, node.val))
        if node.left:
            queue.append((node.left, x - 1, y + 1))
        if node.right:
            queue.append((node.right, x + 1, y + 1))
    node_list.sort()
    res, last_x = [], float('-inf')
    for x, y, val in node_list:
        if x != last_x:
            res.append([])
            last_x = x
        res[-1].append(val)
    return res
