"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 0 <= Node.val <= 10^6

Example:
Input: root = [7,3,15,null,null,9,20]
Output: [3,7,9,15,20]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self._leftmost_inorder(top.right)
        return top.val
    def hasNext(self) -> bool:
        return len(self.stack) > 0

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
    root = list_to_tree([7,3,15,None,None,9,20])
    it = BSTIterator(root)
    while it.hasNext():
        print(it.next(), end=' ')
    # Output: 3 7 9 15 20
