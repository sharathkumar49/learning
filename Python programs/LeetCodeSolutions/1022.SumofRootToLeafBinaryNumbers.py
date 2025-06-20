"""
1022. Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number. Return the sum of these numbers.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Node.val is 0 or 1.

Example:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root: Optional[TreeNode]) -> int:
    def dfs(node, curr):
        if not node:
            return 0
        curr = (curr << 1) | node.val
        if not node.left and not node.right:
            return curr
        return dfs(node.left, curr) + dfs(node.right, curr)
    return dfs(root, 0)

# Example usage:
# Helper to build tree from list
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

root = build_tree([1,0,1,0,1,0,1])
print(sumRootToLeaf(root))  # Output: 22
