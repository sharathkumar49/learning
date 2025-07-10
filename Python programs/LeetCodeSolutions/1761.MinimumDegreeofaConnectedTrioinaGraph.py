"""
LeetCode 1761. Minimum Degree of a Connected Trio in a Graph

Given an undirected graph with n nodes and edges, return the minimum degree of a connected trio in the graph, or -1 if none exists.

Example 1:
Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3

Constraints:
- 2 <= n <= 400
- edges[i].length == 2
- 1 <= edges[i][j] <= n
"""

def minTrioDegree(n, edges):
    g = [set() for _ in range(n+1)]
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)
    res = float('inf')
    for i in range(1, n+1):
        for j in g[i]:
            if j > i:
                for k in g[i] & g[j]:
                    if k > j:
                        res = min(res, len(g[i]) + len(g[j]) + len(g[k]) - 6)
    return res if res != float('inf') else -1

# Example usage:
# n = 6
# edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# print(minTrioDegree(n, edges))  # Output: 3
