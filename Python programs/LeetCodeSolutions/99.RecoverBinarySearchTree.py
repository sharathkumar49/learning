"""
99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Constraints:
- The number of nodes in the tree is in the range [2, 1000].
- -2^31 <= Node.val <= 2^31 - 1

Example:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: Optional[TreeNode]) -> None:
    x = y = prev = None
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev and curr.val < prev.val:
            y = curr
            if not x:
                x = prev
            else:
                break
        prev = curr
        curr = curr.right
    if x and y:
        x.val, y.val = y.val, x.val

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
    def inorder(node):
        return inorder(node.left) + [node.val] if node.left else [] + [node.val] + inorder(node.right) if node.right else [node.val]
    root = list_to_tree([1,3,None,None,2])
    recoverTree(root)
    # Output should be a corrected BST
