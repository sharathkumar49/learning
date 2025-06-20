"""
Find largest value in each tree row (LeetCode 515)
"""
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def largest_values(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level_max = float('-inf')
        for _ in range(len(queue)):
            node = queue.popleft()
            level_max = max(level_max, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level_max)
    return res
