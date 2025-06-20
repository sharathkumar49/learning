"""
310. Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. Given a tree of n nodes labeled from 0 to n - 1, and a list of n - 1 edges, return all the label(s) of the tree's root(s) that result in a minimum height tree.

Constraints:
- 1 <= n <= 2 * 10^4
- edges.length == n - 1
- 0 <= a_i, b_i < n
- a_i != b_i
- All the pairs (a_i, b_i) are distinct.
- The given input is guaranteed to be a tree.
"""
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        from collections import defaultdict, deque
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

# Example usage:
n = 4
edges = [[1,0],[1,2],[1,3]]
print(Solution().findMinHeightTrees(n, edges))  # Output: [1]
