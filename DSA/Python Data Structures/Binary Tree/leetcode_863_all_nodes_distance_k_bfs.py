"""
LeetCode 863: All Nodes Distance K in Binary Tree (Google, Facebook) [BFS Only Version]
Given the root of a binary tree, a target node, and an integer k, return all the values of the nodes that have a distance k from the target node. (BFS only, no graph conversion)
"""
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def distance_k_bfs(root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
    parent = {}
    def dfs(node, par):
        if node:
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root, None)
    queue = deque([(target, 0)])
    seen = {target}
    res = []
    while queue:
        node, dist = queue.popleft()
        if dist == k:
            res.append(node.val)
        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in seen:
                seen.add(nei)
                queue.append((nei, dist + 1))
    return res
