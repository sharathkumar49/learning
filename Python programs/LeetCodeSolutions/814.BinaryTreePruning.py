"""
814. Binary Tree Pruning

Given the root of a binary tree, return the same tree where every subtree not containing a 1 has been removed.

Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]

Example 2:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Constraints:
- The number of nodes in the tree is in the range [1, 200].
- Node.val is 0 or 1.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pruneTree(root):
    if not root:
        return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if root.val == 0 and not root.left and not root.right:
        return None
    return root

# Example usage:
# Helper function to build a tree from list
# ...omitted for brevity...
