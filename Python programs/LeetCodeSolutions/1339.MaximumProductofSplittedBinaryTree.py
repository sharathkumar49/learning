"""
LeetCode 1339. Maximum Product of Splitted Binary Tree

Given the root of a binary tree, split it into two subtrees by removing one edge, and return the maximum product of the sums of the two subtrees. Return the answer modulo 10^9+7.

Constraints:
- The number of nodes in the tree is in the range [2, 5 * 10^4].
- 1 <= Node.val <= 10^4

Example:
Input: root = [1,2,3,4,5,6]
Output: 110
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxProduct(root):
    MOD = 10**9+7
    total = 0
    def get_sum(node):
        nonlocal total
        if not node:
            return 0
        s = node.val + get_sum(node.left) + get_sum(node.right)
        total += node.val
        return s
    total = get_sum(root)
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        s = node.val + dfs(node.left) + dfs(node.right)
        res = max(res, s * (total - s))
        return s
    dfs(root)
    return res % MOD

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
# print(maxProduct(root))  # Output: 110
