"""
LeetCode 230: Kth Smallest Element in a BST
Given the root of a BST, return the kth smallest element.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def kth_smallest(root: BinarySearchTreeNode, k: int) -> int:
    stack = []
    curr = root
    while True:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.data
        curr = curr.right
