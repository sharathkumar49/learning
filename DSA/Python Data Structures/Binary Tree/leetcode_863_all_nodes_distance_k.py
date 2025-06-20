"""
LeetCode 863: All Nodes Distance K in Binary Tree (Google, Facebook)
Given the root of a binary tree, a target node, and an integer k, return all the values of the nodes that have a distance k from the target node.
"""
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def distance_k(root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
    graph = defaultdict(list)
    def build_graph(node, parent):
        if node:
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
    build_graph(root, None)
    visited = set()
    queue = deque([(target, 0)])
    visited.add(target)
    res = []
    while queue:
        node, dist = queue.popleft()
        if dist == k:
            res.append(node.val)
        elif dist < k:
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, dist + 1))
    return res
