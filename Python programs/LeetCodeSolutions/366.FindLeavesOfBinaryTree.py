"""
366. Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if you were doing this: repeatedly remove all leaves, then repeat until the tree is empty.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node):
            if not node:
                return -1
            level = 1 + max(dfs(node.left), dfs(node.right))
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            return level
        dfs(root)
        return res

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# print(Solution().findLeaves(root))  # Output: [[4,5,3],[2],[1]]
