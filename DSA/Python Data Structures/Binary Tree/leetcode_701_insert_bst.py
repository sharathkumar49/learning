"""
LeetCode 701: Insert into a Binary Search Tree (Amazon, Google)
Insert a value into a BST and return the root.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def insert_into_bst(root: BinarySearchTreeNode, val: int) -> BinarySearchTreeNode:
    if not root:
        return BinarySearchTreeNode(val)
    if val < root.data:
        root.left = insert_into_bst(root.left, val)
    elif val > root.data:
        root.right = insert_into_bst(root.right, val)
    return root
