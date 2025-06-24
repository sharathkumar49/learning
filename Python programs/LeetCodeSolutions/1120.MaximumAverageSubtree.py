"""
1120. Maximum Average Subtree

Given the root of a binary tree, return the maximum average value of any subtree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^5

Example:
Input: root = [5,6,1]
Output: 6.00000
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximumAverageSubtree(root: Optional[TreeNode]) -> float:
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return (0, 0)
        lsum, lcnt = dfs(node.left)
        rsum, rcnt = dfs(node.right)
        total = lsum + rsum + node.val
        count = lcnt + rcnt + 1
        res = max(res, total / count)
        return (total, count)
    dfs(root)
    return res

# Example usage:
from collections import deque

def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

root = build_tree([5,6,1])
print(f"{maximumAverageSubtree(root):.5f}")  # Output: 6.00000
