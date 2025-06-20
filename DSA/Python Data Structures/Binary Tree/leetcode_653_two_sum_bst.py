"""
LeetCode 653: Two Sum IV - Input is a BST
Given the root of a BST and an integer k, return true if there exist two elements in the BST such that their sum is equal to k.
Uses BinarySearchTreeNode from your base implementation.
"""
from binarysearchtree import BinarySearchTreeNode

def find_target(root: BinarySearchTreeNode, k: int) -> bool:
    seen = set()
    def dfs(node):
        if not node:
            return False
        if k - node.data in seen:
            return True
        seen.add(node.data)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)
