"""
LeetCode 1973. Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value is equal to the average of the values in its subtree.

Example:
Input: root = [4,8,5,0,1,null,6]
Output: 5

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfSubtree(root):
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return (0, 0)
        s1, c1 = dfs(node.left)
        s2, c2 = dfs(node.right)
        s, c = s1 + s2 + node.val, c1 + c2 + 1
        if node.val == s // c:
            res += 1
        return (s, c)
    dfs(root)
    return res

# Example usage:
# root = TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
# print(averageOfSubtree(root))  # Output: 5
