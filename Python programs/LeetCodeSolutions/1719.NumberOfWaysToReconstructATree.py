"""
LeetCode 1719. Number Of Ways To Reconstruct A Tree

Given pairs of parent-child relationships, return the number of ways to reconstruct the tree (0, 1, or 2).

Example 1:
Input: pairs = [[1,2],[2,3]]
Output: 1

Constraints:
- 1 <= pairs.length <= 10^5
- 1 <= pairs[i][0], pairs[i][1] <= 500
"""

def checkWays(pairs):
    from collections import defaultdict
    adj = defaultdict(set)
    for u, v in pairs:
        adj[u].add(v)
        adj[v].add(u)
    nodes = sorted(adj, key=lambda x: -len(adj[x]))
    root = nodes[0]
    for node in nodes:
        if node == root:
            continue
        parent = None
        min_size = float('inf')
        for nei in adj[node]:
            if len(adj[nei]) >= len(adj[node]) and len(adj[nei]) < min_size:
                min_size = len(adj[nei])
                parent = nei
        if parent is None:
            return 0
        if not adj[node] - {parent} <= adj[parent]:
            return 0
    res = 1
    for node in nodes[1:]:
        parent = None
        min_size = float('inf')
        for nei in adj[node]:
            if len(adj[nei]) >= len(adj[node]) and len(adj[nei]) < min_size:
                min_size = len(adj[nei])
                parent = nei
        if len(adj[parent]) == len(adj[node]):
            res = 2
    return res

# Example usage:
# pairs = [[1,2],[2,3]]
# print(checkWays(pairs))  # Output: 1
