"""
LeetCode 235: Lowest Common Ancestor of a BST
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def lowest_common_ancestor(root: BinarySearchTreeNode, p: int, q: int) -> BinarySearchTreeNode:
    curr = root
    while curr:
        if p < curr.data and q < curr.data:
            curr = curr.left
        elif p > curr.data and q > curr.data:
            curr = curr.right
        else:
            return curr
    return None
