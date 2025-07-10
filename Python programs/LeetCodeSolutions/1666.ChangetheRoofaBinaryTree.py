"""
LeetCode 1666. Change the Root of a Binary Tree

Given the root of a binary tree and a leaf node, change the root to the leaf and return the new root.

Example 1:
Input: root = [1,2,3], leaf = 3
Output: [3,1,2]

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
"""

def changeRoot(root, leaf):
    def dfs(node, parent):
        if not node:
            return False
        if node == leaf:
            node.left = parent
            return True
        if dfs(node.left, node):
            node.left = parent
            return True
        if dfs(node.right, node):
            node.right = parent
            return True
        return False
    dfs(root, None)
    return leaf

# Example usage:
# (Assume TreeNode class is defined)
# root = ...
# leaf = ...
# print(changeRoot(root, leaf))
