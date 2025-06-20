"""
572. Subtree of Another Tree
Difficulty: Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [1,2,3], subRoot = [1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [1, 2000].
-10^4 <= Node.val <= 10^4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    def isSame(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)
    if not root:
        return False
    if isSame(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# Example usage
# (See LeetCode for binary tree construction examples)
