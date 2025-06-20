"""
993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

Given the root of a binary tree with unique values and two integers x and y, return true if the nodes with values x and y are cousins. Two nodes are cousins if they have the same depth but different parents.

Constraints:
- The number of nodes in the tree is in the range [2, 100].
- 1 <= Node.val <= 100
- Each node has a unique value.
- x != y

Example:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth):
            if not node:
                return None
            if node.val == x or node.val == y:
                return (parent, depth)
            left = dfs(node.left, node, depth+1)
            right = dfs(node.right, node, depth+1)
            return left or right
        px, dx = dfs(root, None, 0)
        py, dy = dfs(root, None, 0)
        return dx == dy and px != py

# Example usage (constructs tree and checks cousins)
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    x = 4
    y = 3
    print(Solution().isCousins(root, x, y))  # Output: False
