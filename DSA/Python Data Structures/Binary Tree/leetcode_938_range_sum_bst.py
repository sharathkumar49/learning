"""
LeetCode 938: Range Sum of BST
Given the root of a BST, return the sum of values of all nodes with value in the range [low, high].
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def range_sum_bst(root: BinarySearchTreeNode, low: int, high: int) -> int:
    if not root:
        return 0
    if root.data < low:
        return range_sum_bst(root.right, low, high)
    if root.data > high:
        return range_sum_bst(root.left, low, high)
    return root.data + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)
