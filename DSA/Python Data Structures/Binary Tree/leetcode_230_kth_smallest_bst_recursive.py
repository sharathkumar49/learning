"""
LeetCode 230: Kth Smallest Element in a BST (Amazon, Google) [Recursive Version]
Given the root of a BST, return the kth smallest element (recursive approach).
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def kth_smallest_recursive(root: BinarySearchTreeNode, k: int) -> int:
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.data] + inorder(node.right)
    return inorder(root)[k-1]
