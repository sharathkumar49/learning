"""
Find duplicate subtrees (LeetCode 652)
Return all duplicate subtrees. For each kind of duplicate subtrees, only one of them needs to be returned.
"""
from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def find_duplicate_subtrees(root: Optional[TreeNode]) -> List[TreeNode]:
    count = defaultdict(int)
    res = []
    def collect(node):
        if not node:
            return '#'
        serial = f'{node.val},{collect(node.left)},{collect(node.right)}'
        count[serial] += 1
        if count[serial] == 2:
            res.append(node)
        return serial
    collect(root)
    return res
