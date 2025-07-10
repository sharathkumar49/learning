"""
LeetCode 1457. Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9, return the number of pseudo-palindromic paths from root to leaf. A path is pseudo-palindromic if at most one digit occurs an odd number of times along the path.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 9

Example:
Input: root = [2,3,1,3,1,null,1]
Output: 2
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pseudoPalindromicPaths(root):
    def dfs(node, path):
        if not node:
            return 0
        path ^= 1 << node.val
        if not node.left and not node.right:
            return int(path & (path - 1) == 0)
        return dfs(node.left, path) + dfs(node.right, path)
    return dfs(root, 0)

# Example usage:
# root = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
# print(pseudoPalindromicPaths(root))  # Output: 2
