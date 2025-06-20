"""
545. Boundary of Binary Tree

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from the root.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -1000 <= Node.val <= 1000

Example:
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> list:
        if not root:
            return []
        res = [root.val]
        def leftBoundary(node):
            if node and (node.left or node.right):
                res.append(node.val)
                if node.left:
                    leftBoundary(node.left)
                else:
                    leftBoundary(node.right)
        def leaves(node):
            if node:
                leaves(node.left)
                if not node.left and not node.right and node != root:
                    res.append(node.val)
                leaves(node.right)
        def rightBoundary(node):
            if node and (node.left or node.right):
                if node.right:
                    rightBoundary(node.right)
                else:
                    rightBoundary(node.left)
                res.append(node.val)
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return res

# Example usage:
root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
sol = Solution()
print(sol.boundaryOfBinaryTree(root))  # Output: [1, 3, 4, 2]
