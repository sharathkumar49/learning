"""
968. Binary Tree Cameras
https://leetcode.com/problems/binary-tree-cameras/

Given the root of a binary tree, return the minimum number of cameras needed to monitor all nodes of the tree. Each camera at a node can monitor its parent, itself, and its immediate children.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Node.val == 0

Example:
Input: root = [0,0,null,0,0]
Output: 1
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 1
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                res += 1
                return 2
            if l == 2 or r == 2:
                return 1
            return 0
        return (dfs(root) == 0) + res

# Example usage (constructs tree and prints min cameras)
if __name__ == "__main__":
    root = TreeNode(0, TreeNode(0, None, TreeNode(0, TreeNode(0), None)), None)
    print(Solution().minCameraCover(root))  # Output: 1
