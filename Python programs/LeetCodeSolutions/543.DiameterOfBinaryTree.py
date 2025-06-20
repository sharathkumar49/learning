"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100

Example:
Input: root = [1,2,3,4,5]
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l + r)
            return max(l, r) + 1
        depth(root)
        return self.ans

# Example usage:
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3
