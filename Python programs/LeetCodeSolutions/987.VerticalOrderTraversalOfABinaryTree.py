"""
987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Given the root of a binary tree, return the vertical order traversal of its nodes' values. Nodes are reported by column, from left to right, and within each column by row, from top to bottom. If two nodes are in the same row and column, order them by their value.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 1000

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
"""
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root, 0, 0)
        nodes.sort()
        res = []
        last_col = float('-inf')
        for col, row, val in nodes:
            if col != last_col:
                res.append([])
                last_col = col
            res[-1].append(val)
        return res

# Example usage (constructs tree and prints vertical order)
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().verticalTraversal(root))  # Output: [[9],[3,15],[20],[7]]
