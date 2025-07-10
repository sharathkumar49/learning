"""
LeetCode 1644. Lowest Common Ancestor of a Binary Tree II

Given the root of a binary tree and two nodes p and q, return their lowest common ancestor. If either node does not exist, return None.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- -10^9 <= Node.val <= 10^9
"""

def lowestCommonAncestor(root, p, q):
    def dfs(node):
        if not node:
            return (None, False, False)
        lca, f1, f2 = dfs(node.left)
        if lca:
            return (lca, True, True)
        rca, r1, r2 = dfs(node.right)
        if rca:
            return (rca, True, True)
        f1 = f1 or r1 or node == p
        f2 = f2 or r2 or node == q
        if f1 and f2:
            return (node, True, True)
        return (None, f1, f2)
    lca, f1, f2 = dfs(root)
    return lca if f1 and f2 else None

# Example usage:
# (Assume TreeNode class is defined)
# root = ...
# p = ...
# q = ...
# print(lowestCommonAncestor(root, p, q))
