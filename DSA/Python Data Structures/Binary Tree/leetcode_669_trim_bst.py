"""
LeetCode 669: Trim a Binary Search Tree (Google, Facebook)
Given the root of a BST and the range [low, high], trim the tree so that all its elements lie in [low, high].
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def trim_bst(root: BinarySearchTreeNode, low: int, high: int) -> BinarySearchTreeNode:
    if not root:
        return None
    if root.data < low:
        return trim_bst(root.right, low, high)
    if root.data > high:
        return trim_bst(root.left, low, high)
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root
