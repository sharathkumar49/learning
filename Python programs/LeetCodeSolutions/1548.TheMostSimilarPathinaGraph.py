"""
LeetCode 1548. The Most Similar Path in a Graph

Given a graph and a target path, return the path in the graph that is most similar to the target path.

Constraints:
- 2 <= n <= 100
- 1 <= roads.length <= n * (n - 1) / 2
- 1 <= targetPath.length <= 100

Example:
Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,0],[2,1],[2,4],[3,0],[3,1],[4,1],[4,2]], names = ["A","B","C","D","E"], targetPath = ["A","B","C","B","C","D"]
Output: [0,1,2,1,2,3]
"""
def mostSimilar(n, roads, names, targetPath):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    m = len(targetPath)
    dp = [[float('inf')]*n for _ in range(m)]
    path = [[-1]*n for _ in range(m)]
    for i in range(n):
        dp[0][i] = (names[i] != targetPath[0])
    for i in range(1, m):
        for v in range(n):
            for u in graph[v]:
                cost = dp[i-1][u] + (names[v] != targetPath[i])
                if cost < dp[i][v]:
                    dp[i][v] = cost
                    path[i][v] = u
    idx = min(range(n), key=lambda x: dp[m-1][x])
    res = [0]*m
    for i in range(m-1, -1, -1):
        res[i] = idx
        idx = path[i][idx]
    return res

# Example usage:
n = 5
roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,0],[2,1],[2,4],[3,0],[3,1],[4,1],[4,2]]
names = ["A","B","C","D","E"]
targetPath = ["A","B","C","B","C","D"]
print(mostSimilar(n, roads, names, targetPath))  # Output: [0,1,2,1,2,3]
