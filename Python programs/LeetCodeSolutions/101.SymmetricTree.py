"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    return isMirror(root, root)

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
    root = list_to_tree([1,2,2,3,4,4,3])
    print(isSymmetric(root))  # Output: True
    root2 = list_to_tree([1,2,2,None,3,None,3])
    print(isSymmetric(root2)) # Output: False
