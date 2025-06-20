"""
LeetCode 173: BST Iterator
Implement an iterator over a BST with next() and hasNext().
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

class BSTIterator:
    def __init__(self, root: BinarySearchTreeNode):
        self.stack = []
        self._push_left(root)
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def hasNext(self) -> bool:
        return bool(self.stack)
    def next(self) -> int:
        node = self.stack.pop()
        val = node.data
        self._push_left(node.right)
        return val
