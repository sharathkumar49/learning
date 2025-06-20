"""
538. Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^4 <= Node.val <= 10^4
- All the values are unique.

Example:
Input: root = [5,2,13]
Output: [18,20,13]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.total += node.val
            node.val = self.total
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root

# Example usage:
root = TreeNode(5, TreeNode(2), TreeNode(13))
sol = Solution()
root = sol.convertBST(root)
print(root.val)  # Output: 18
