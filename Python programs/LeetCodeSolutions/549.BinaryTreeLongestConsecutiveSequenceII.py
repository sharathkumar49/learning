"""
549. Binary Tree Longest Consecutive Sequence II

Given the root of a binary tree, return the length of the longest consecutive path in the tree. The path can be either increasing or decreasing.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -3 * 10^4 <= Node.val <= 3 * 10^4

Example:
Input: root = [1,2,3]
Output: 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return (0, 0)
            inc, dec = 1, 1
            if node.left:
                l_inc, l_dec = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = l_dec + 1
                elif node.val == node.left.val - 1:
                    inc = l_inc + 1
            if node.right:
                r_inc, r_dec = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, r_dec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, r_inc + 1)
            self.ans = max(self.ans, inc + dec - 1)
            return (inc, dec)
        dfs(root)
        return self.ans

# Example usage:
root = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
print(sol.longestConsecutive(root))  # Output: 2
