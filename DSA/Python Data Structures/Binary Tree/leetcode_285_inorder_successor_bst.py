"""
LeetCode 285: Inorder Successor in BST (Google, Facebook)
Given the root of a BST and a node p, return the inorder successor of node p in the BST.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def inorder_successor(root: BinarySearchTreeNode, p: BinarySearchTreeNode) -> BinarySearchTreeNode:
    succ = None
    curr = root
    while curr:
        if p.data < curr.data:
            succ = curr
            curr = curr.left
        else:
            curr = curr.right
    return succ
