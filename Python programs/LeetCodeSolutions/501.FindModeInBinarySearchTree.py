"""
501. Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (the most frequently occurred element) in the BST.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Example:
Input: root = [1,null,2,2]
Output: [2]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> list:
        self.count = self.max_count = 0
        self.prev = None
        self.modes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return list(set(self.modes))

# Example usage:
root = TreeNode(1, None, TreeNode(2, TreeNode(2)))
sol = Solution()
print(sol.findMode(root))  # Output: [2]
