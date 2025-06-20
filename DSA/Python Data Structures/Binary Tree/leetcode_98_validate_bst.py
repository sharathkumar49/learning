"""
LeetCode 98: Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid BST.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def is_valid_bst(root: BinarySearchTreeNode, low=float('-inf'), high=float('inf')) -> bool:
    if not root:
        return True
    if not (low < root.data < high):
        return False
    return is_valid_bst(root.left, low, root.data) and is_valid_bst(root.right, root.data, high)
