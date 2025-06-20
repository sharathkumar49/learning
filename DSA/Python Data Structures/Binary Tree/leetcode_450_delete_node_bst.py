"""
LeetCode 450: Delete Node in a BST
Delete a node from a BST and return its root.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def delete_node(root: BinarySearchTreeNode, key: int) -> BinarySearchTreeNode:
    if not root:
        return None
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root
