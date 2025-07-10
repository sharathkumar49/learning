"""
LeetCode 1740. Find Distance in a Binary Tree

Given the root of a binary tree and two integers p and q, return the distance between the nodes with values p and q.

Example 1:
Input: root = [1,2,3,4], p = 4, q = 3
Output: 3

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
- All Node.val are unique.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDistance(root, p, q):
    def dfs(node):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        l = dfs(node.left)
        r = dfs(node.right)
        if l and r:
            return node
        return l or r
    def path(node, val):
        if not node:
            return []
        if node.val == val:
            return [node]
        left = path(node.left, val)
        if left:
            return [node] + left
        right = path(node.right, val)
        if right:
            return [node] + right
        return []
    lca = dfs(root)
    path_p = path(lca, p)
    path_q = path(lca, q)
    return len(path_p) + len(path_q) - 2

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
# p = 4
# q = 3
# print(findDistance(root, p, q))  # Output: 3
