"""
971. Flip Binary Tree To Match Preorder Traversal
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

Given the root of a binary tree with N nodes, each node has a distinct value from 1 to N. A node can flip its left and right child. Return a list of the values of nodes flipped to match the given voyage (preorder traversal). If it is impossible, return [-1].

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 1 <= Node.val <= 100
- All Node.val are unique.

Example:
Input: root = [1,2], voyage = [2,1]
Output: [-1]
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = []
        self.i = 0
        def dfs(node):
            if not node:
                return True
            if node.val != voyage[self.i]:
                return False
            self.i += 1
            if node.left and self.i < len(voyage) and node.left.val != voyage[self.i]:
                res.append(node.val)
                node.left, node.right = node.right, node.left
            return dfs(node.left) and dfs(node.right)
        return res if dfs(root) else [-1]

# Example usage (constructs tree and prints flips)
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2))
    voyage = [2,1]
    print(Solution().flipMatchVoyage(root, voyage))  # Output: [-1]
