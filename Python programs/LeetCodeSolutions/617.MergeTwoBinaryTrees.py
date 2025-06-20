"""
617. Merge Two Binary Trees
Difficulty: Easy

Given two binary trees root1 and root2, merge them into a new binary tree. The new tree's value at each node is the sum of the values of the corresponding nodes of the input trees. If only one node exists, use its value.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Constraints:
The number of nodes in both trees is in the range [0, 2000].
-10^4 <= Node.val <= 10^4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None
    val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
    left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return TreeNode(val, left, right)

# Example usage
# (See LeetCode for binary tree construction examples)
