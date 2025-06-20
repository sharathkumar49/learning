"""
LeetCode 938: Range Sum of BST (Amazon, Google) [Iterative Version]
Given the root of a BST, return the sum of values of all nodes with value in the range [low, high] (iterative approach).
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def range_sum_bst_iterative(root: BinarySearchTreeNode, low: int, high: int) -> int:
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        if low <= node.data <= high:
            total += node.data
        if node.left and node.data > low:
            stack.append(node.left)
        if node.right and node.data < high:
            stack.append(node.right)
    return total
