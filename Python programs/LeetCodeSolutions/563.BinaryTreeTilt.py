"""
563. Binary Tree Tilt
Difficulty: Easy

Given the root of a binary tree, return the tilt of the whole tree.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null nodes have tilt 0.
The tilt of the whole tree is the sum of all nodes' tilt.

Example 1:
Input: root = [1,2,3]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTilt(root):
    total = 0
    def dfs(node):
        nonlocal total
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        total += abs(left - right)
        return left + right + node.val
    dfs(root)
    return total

# Example usage
# (See LeetCode for binary tree construction examples)
