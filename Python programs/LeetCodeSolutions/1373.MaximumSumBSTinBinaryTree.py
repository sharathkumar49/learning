"""
LeetCode 1373. Maximum Sum BST in Binary Tree

Given the root of a binary tree, return the maximum sum of all keys of any sub-tree which is a Binary Search Tree (BST).

Constraints:
- The number of nodes in the tree is in the range [1, 4 * 10^4].
- -10^4 <= Node.val <= 10^4

Example:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSumBST(root):
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return (True, float('inf'), float('-inf'), 0)
        l_bst, l_min, l_max, l_sum = dfs(node.left)
        r_bst, r_min, r_max, r_sum = dfs(node.right)
        if l_bst and r_bst and l_max < node.val < r_min:
            s = l_sum + r_sum + node.val
            res = max(res, s)
            return (True, min(l_min, node.val), max(r_max, node.val), s)
        return (False, 0, 0, 0)
    dfs(root)
    return res

# Example usage:
# Not provided due to complexity of tree construction.
