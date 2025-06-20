"""
LeetCode 863: All Nodes Distance K in Binary Tree (Google, Facebook) [DFS Only Version]
Given the root of a binary tree, a target node, and an integer k, return all the values of the nodes that have a distance k from the target node. (DFS only, no graph conversion)
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def distance_k_dfs(root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
    res = []
    def subtree_add(node, dist):
        if not node:
            return
        if dist == k:
            res.append(node.val)
        else:
            subtree_add(node.left, dist + 1)
            subtree_add(node.right, dist + 1)
    def dfs(node):
        if not node:
            return -1
        if node == target:
            subtree_add(node, 0)
            return 1
        L = dfs(node.left)
        R = dfs(node.right)
        if L != -1:
            if L == k:
                res.append(node.val)
            subtree_add(node.right, L + 1)
            return L + 1
        if R != -1:
            if R == k:
                res.append(node.val)
            subtree_add(node.left, R + 1)
            return R + 1
        return -1
    dfs(root)
    return res
