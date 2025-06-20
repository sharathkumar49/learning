"""
951. Flip Equivalent Binary Trees
https://leetcode.com/problems/flip-equivalent-binary-trees/

For a binary tree T, we can flip the left and right child of any node. Two binary trees are flip equivalent if they are the same after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent, otherwise false.

Constraints:
- The number of nodes in each tree is in the range [0, 100].
- Each node's value is a unique integer in the range [0, 99].

Example:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
                (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))

# Example usage (constructs trees and checks equivalence)
if __name__ == "__main__":
    def build_tree1():
        n7 = TreeNode(7)
        n8 = TreeNode(8)
        n5 = TreeNode(5, n7, n8)
        n6 = TreeNode(6)
        n4 = TreeNode(4)
        n2 = TreeNode(2, n4, n5)
        n3 = TreeNode(3, n6)
        n1 = TreeNode(1, n2, n3)
        return n1
    def build_tree2():
        n8 = TreeNode(8)
        n7 = TreeNode(7)
        n5 = TreeNode(5, n8, n7)
        n6 = TreeNode(6)
        n4 = TreeNode(4)
        n2 = TreeNode(2, n5, n4)
        n3 = TreeNode(3, None, n6)
        n1 = TreeNode(1, n3, n2)
        return n1
    root1 = build_tree1()
    root2 = build_tree2()
    print(Solution().flipEquiv(root1, root2))  # Output: True
