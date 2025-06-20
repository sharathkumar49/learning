"""
606. Construct String from Binary Tree
Difficulty: Easy

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping between the string and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-1000 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root):
    if not root:
        return ''
    left = f'({tree2str(root.left)})' if root.left or root.right else ''
    right = f'({tree2str(root.right)})' if root.right else ''
    return f'{root.val}{left}{right}'

# Example usage
# (See LeetCode for binary tree construction examples)
