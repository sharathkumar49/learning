"""
156. Binary Tree Upside Down
https://leetcode.com/problems/binary-tree-upside-down/

Given the root of a binary tree, turn the tree upside down and return the new root.

Constraints:
- The number of nodes in the tree is in the range [0, 10^0].
- -100 <= Node.val <= 100

Example:
Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def upsideDownBinaryTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root or not root.left:
        return root
    new_root = upsideDownBinaryTree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return new_root

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
    root = list_to_tree([1,2,3,4,5])
    new_root = upsideDownBinaryTree(root)
    # Output: new_root is the root of the upside down tree
