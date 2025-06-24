"""
LeetCode 1315. Sum of Nodes with Even-Valued Grandparent

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 100

Example:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root):
    def dfs(node, parent, grandparent):
        if not node:
            return 0
        res = 0
        if grandparent and grandparent.val % 2 == 0:
            res += node.val
        res += dfs(node.left, node, parent)
        res += dfs(node.right, node, parent)
        return res
    return dfs(root, None, None)

# Example usage:
# root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
# print(sumEvenGrandparent(root))  # Output: 18
