"""
965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/

A binary tree is univalued if every node in the tree has the same value. Given the root of a binary tree, return true if the tree is univalued, or false otherwise.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val < 100

Example:
Input: root = [1,1,1,1,1,null,1]
Output: true
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

# Example usage (constructs tree and checks if univalued)
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), None)
    print(Solution().isUnivalTree(root))  # Output: True
