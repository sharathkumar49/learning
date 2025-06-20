"""
LeetCode 1038: Binary Search Tree to Greater Sum Tree (Amazon, Google)
Given the root of a BST, convert it to a Greater Sum Tree where every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def bst_to_gst(root: BinarySearchTreeNode) -> BinarySearchTreeNode:
    total = 0
    def reverse_inorder(node):
        nonlocal total
        if not node:
            return
        reverse_inorder(node.right)
        total += node.data
        node.data = total
        reverse_inorder(node.left)
    reverse_inorder(root)
    return root
