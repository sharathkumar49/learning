"""
LeetCode 700: Search in a Binary Search Tree (Amazon, Google)
Given the root of a BST and a value, return the node where value == val, or None if not found.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def search_bst(root: BinarySearchTreeNode, val: int) -> BinarySearchTreeNode:
    if not root or root.data == val:
        return root
    if val < root.data:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
