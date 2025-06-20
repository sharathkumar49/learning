"""
783. Minimum Distance Between BST Nodes

Given the root of a Binary Search Tree (BST) with values in the range [0, 100000], return the minimum difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [2, 100].
- 0 <= Node.val <= 10^5
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root):
    prev = None
    min_diff = float('inf')
    def inorder(node):
        nonlocal prev, min_diff
        if not node:
            return
        inorder(node.left)
        if prev is not None:
            min_diff = min(min_diff, node.val - prev)
        prev = node.val
        inorder(node.right)
    inorder(root)
    return min_diff

# Example usage:
# Helper function to build a BST from list
# ...omitted for brevity...
