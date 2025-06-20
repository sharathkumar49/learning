"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Example:
Input: root = [2,1,3]
Output: true
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root, float('-inf'), float('inf'))

# Example usage:
if __name__ == "__main__":
    def list_to_tree(lst):
        if not lst:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root
    root = list_to_tree([2,1,3])
    print(isValidBST(root))  # Output: True
    root = list_to_tree([5,1,4,None,None,3,6])
    print(isValidBST(root))  # Output: False
