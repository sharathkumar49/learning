"""
LeetCode 501: Find Mode in Binary Search Tree
Given the root of a BST, return all the mode(s) (the most frequently occurred element) in the BST.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode
from typing import List

def find_mode(root: BinarySearchTreeNode) -> List[int]:
    modes = []
    prev = [None]
    count = [0]
    max_count = [0]
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        if prev[0] == node.data:
            count[0] += 1
        else:
            count[0] = 1
        if count[0] > max_count[0]:
            max_count[0] = count[0]
            modes.clear()
            modes.append(node.data)
        elif count[0] == max_count[0]:
            modes.append(node.data)
        prev[0] = node.data
        inorder(node.right)
    inorder(root)
    return modes
