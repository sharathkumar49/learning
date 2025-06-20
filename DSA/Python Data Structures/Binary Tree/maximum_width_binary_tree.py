"""
Maximum width of binary tree (LeetCode 662)
Return the maximum width of a binary tree.
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def width_of_binary_tree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    max_width = 0
    queue = deque([(root, 0)])
    while queue:
        level_length = len(queue)
        _, first_index = queue[0]
        for _ in range(level_length):
            node, idx = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * idx))
            if node.right:
                queue.append((node.right, 2 * idx + 1))
        max_width = max(max_width, idx - first_index + 1)
    return max_width
