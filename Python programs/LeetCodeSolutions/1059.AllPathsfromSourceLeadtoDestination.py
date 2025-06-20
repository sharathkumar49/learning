"""
1059. All Paths from Source Lead to Destination

Given a directed, acyclic graph with n nodes, return true if and only if all paths from source lead to destination.

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 2000
- 0 <= edges[i][j] < n
- 0 <= source, destination < n

Example:
Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false
"""
from typing import List

def leadsToDestination(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    visited = [0] * n
    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True
        if not graph[node]:
            return node == destination
        visited[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        visited[node] = 2
        return True
    return dfs(source)

# Example usage:
n = 4
edges = [[0,1],[0,3],[1,2],[2,1]]
source = 0
destination = 3
print(leadsToDestination(n, edges, source, destination))  # Output: False
