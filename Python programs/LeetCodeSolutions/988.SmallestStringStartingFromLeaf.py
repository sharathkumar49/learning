"""
988. Smallest String Starting From Leaf
https://leetcode.com/problems/smallest-string-starting-from-leaf/

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z'. Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

Constraints:
- The number of nodes in the tree is in the range [1, 8500].
- 0 <= Node.val <= 25

Example:
Input: root = [0,1,2,3,4,3,4]
Output: "dba"
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "~"
        def dfs(node, path):
            if not node:
                return
            path = chr(ord('a') + node.val) + path
            if not node.left and not node.right:
                if path < self.ans:
                    self.ans = path
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, "")
        return self.ans

# Example usage (constructs tree and prints smallest string)
if __name__ == "__main__":
    root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
    print(Solution().smallestFromLeaf(root))  # Output: "dba"
