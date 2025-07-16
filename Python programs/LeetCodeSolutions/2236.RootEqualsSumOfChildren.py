"""
LeetCode 2236. Root Equals Sum of Children

Given the root of a binary tree, return true if root.val == root.left.val + root.right.val.

Example:
Input: root = [10,4,6]
Output: True

Constraints:
- The tree has only 3 nodes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root):
    return root.val == root.left.val + root.right.val

# Example usage:
# root = TreeNode(10, TreeNode(4), TreeNode(6))
# print(checkTree(root))  # Output: True
