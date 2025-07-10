"""
LeetCode 1786. Number of Restricted Paths From First to Last Node

Given a weighted, undirected, connected graph, return the number of restricted paths from node 1 to node n.

Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3

Constraints:
- 1 <= n <= 2 * 10^4
- edges.length == m
- 1 <= ui, vi <= n
- 1 <= weighti <= 10^5
"""

def countRestrictedPaths(n, edges):
    import heapq
    from collections import defaultdict
    MOD = 10**9+7
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    dist = [float('inf')] * (n+1)
    dist[n] = 0
    hq = [(0, n)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(hq, (dist[v], v))
    dp = [0] * (n+1)
    dp[n] = 1
    nodes = list(range(1, n+1))
    nodes.sort(key=lambda x: dist[x])
    for u in nodes:
        for v, _ in g[u]:
            if dist[u] > dist[v]:
                dp[u] = (dp[u] + dp[v]) % MOD
    return dp[1]

# Example usage:
# n = 5
# edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
# print(countRestrictedPaths(n, edges))  # Output: 3
