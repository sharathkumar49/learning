"""
776. Split BST

Given the root of a Binary Search Tree (BST) and an integer target, split the tree into two subtrees: one with all nodes less than or equal to target, and the other with all nodes greater than target. Return the roots of the two subtrees as a list.

Example 1:
Input: root = [4,2,6,1,3,5,7], target = 2
Output: [[2,1],[4,3,6,5,7]]

Constraints:
- The number of nodes in the tree is in the range [1, 50].
- 0 <= Node.val <= 1000
- All Node.val are unique.
- The tree is a valid BST.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def splitBST(root, target):
    if not root:
        return [None, None]
    if root.val <= target:
        left, right = splitBST(root.right, target)
        root.right = left
        return [root, right]
    else:
        left, right = splitBST(root.left, target)
        root.left = right
        return [left, root]

# Example usage:
# Helper function to build a BST from list
# ...omitted for brevity...
