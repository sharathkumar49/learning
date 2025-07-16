"""
LeetCode 2331. Evaluate Boolean Binary Tree

Given the root of a binary tree, return the boolean result of evaluating the tree.

Example:
Input: root = [2,1,3,null,null,0,1]
Output: True

Constraints:
- The number of nodes in the tree is in the range [1, 1000]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root):
    if not root.left and not root.right:
        return bool(root.val)
    if root.val == 2:
        return evaluateTree(root.left) or evaluateTree(root.right)
    if root.val == 3:
        return evaluateTree(root.left) and evaluateTree(root.right)

# Example usage:
# root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
# print(evaluateTree(root))  # Output: True
