"""
LeetCode 1676. Lowest Common Ancestor of a Binary Tree IV

Given the root of a binary tree and a list of nodes, return their lowest common ancestor.

Example 1:
Input: root = [1,2,3], nodes = [2,3]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^9 <= Node.val <= 10^9
"""

def lowestCommonAncestor(root, nodes):
    nodes = set(nodes)
    def dfs(node):
        if not node or node in nodes:
            return node
        l = dfs(node.left)
        r = dfs(node.right)
        if l and r:
            return node
        return l or r
    return dfs(root)

# Example usage:
# (Assume TreeNode class is defined)
# root = ...
# nodes = ...
# print(lowestCommonAncestor(root, nodes))
