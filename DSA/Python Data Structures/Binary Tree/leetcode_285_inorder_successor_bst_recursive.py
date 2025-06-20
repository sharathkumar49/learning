"""
LeetCode 285: Inorder Successor in BST (Google, Facebook) [Recursive Version]
Given the root of a BST and a node p, return the inorder successor of node p in the BST (recursive approach).
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def inorder_successor_recursive(root: BinarySearchTreeNode, p: BinarySearchTreeNode) -> BinarySearchTreeNode:
    if not root:
        return None
    if root.data <= p.data:
        return inorder_successor_recursive(root.right, p)
    left = inorder_successor_recursive(root.left, p)
    return left if left else root
