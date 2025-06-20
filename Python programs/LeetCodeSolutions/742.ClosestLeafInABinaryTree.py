"""
LeetCode 742. Closest Leaf in a Binary Tree

Given the root of a binary tree and an integer k, return the value of the closest leaf to the node with value k in the tree.

Example 1:
Input: root = [1,3,2], k = 1
Output: 2

Example 2:
Input: root = [1], k = 1
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 1 <= Node.val <= 1000
- All the values of the tree are unique.
- root is guaranteed to be a valid binary tree.
- 1 <= k <= 1000
"""
from typing import Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestLeaf(root: Optional[TreeNode], k: int) -> int:
    graph = defaultdict(list)
    def dfs(node, parent=None):
        if node:
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)
    queue = deque([k])
    visited = set()
    while queue:
        node = queue.popleft()
        visited.add(node)
        is_leaf = True
        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
                is_leaf = False
        if is_leaf:
            return node
    return -1

# Example usage
if __name__ == "__main__":
    def build_tree(vals):
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root
    root = build_tree([1,3,2])
    print(findClosestLeaf(root, 1))  # Output: 2
    root = build_tree([1])
    print(findClosestLeaf(root, 1))  # Output: 1
