"""
998. Maximum Binary Tree II
https://leetcode.com/problems/maximum-binary-tree-ii/

A maximum tree is a tree where every node has a value greater than any other value in its subtree. Given the root of a maximum binary tree and a value val, insert val into the tree and return the root of the tree after insertion.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 1 <= Node.val, val <= 100
- All Node.val are unique.

Example:
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val > root.val:
            return TreeNode(val, root)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root

# Example usage (constructs tree and inserts value)
if __name__ == "__main__":
    root = TreeNode(4, TreeNode(1), TreeNode(3, TreeNode(2)))
    val = 5
    new_root = Solution().insertIntoMaxTree(root, val)
    print(new_root.val)  # Output: 5
