"""
LeetCode 1372. Longest ZigZag Path in a Binary Tree

Given the root of a binary tree, return the length of the longest ZigZag path in the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 100

Example:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestZigZag(root):
    res = 0
    def dfs(node, left, right):
        nonlocal res
        if not node:
            return
        res = max(res, left, right)
        dfs(node.left, right+1, 0)
        dfs(node.right, 0, left+1)
    dfs(root, 0, 0)
    return res

# Example usage:
# Not provided due to complexity of tree construction.
