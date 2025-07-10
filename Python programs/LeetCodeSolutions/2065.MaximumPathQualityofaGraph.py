"""
LeetCode 2065. Maximum Path Quality of a Graph

Given a graph, values for each node, and time constraints, return the maximum path quality.

Example:
Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
Output: 75

Constraints:
- 1 <= values.length <= 100
- 0 <= values[i] <= 1000
- 0 <= edges.length <= 200
- 1 <= maxTime <= 100
"""

def maximalPathQuality(values, edges, maxTime):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))
    res = 0
    n = len(values)
    def dfs(u, time, score, visited):
        nonlocal res
        if time > maxTime:
            return
        if u == 0:
            res = max(res, score)
        for v, t in graph[u]:
            if visited[v]:
                dfs(v, time + t, score, visited)
            else:
                visited[v] = 1
                dfs(v, time + t, score + values[v], visited)
                visited[v] = 0
    visited = [0] * n
    visited[0] = 1
    dfs(0, 0, values[0], visited)
    return res

# Example usage:
# print(maximalPathQuality([0,32,10,43], [[0,1,10],[1,2,15],[0,3,10]], 49))  # Output: 75
