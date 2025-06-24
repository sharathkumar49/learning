"""
LeetCode 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

Given n cities and edges, return the city with the smallest number of neighbors at a distance <= threshold. If multiple, return the greatest city number.

Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= n*(n-1)/2
- edges[i].length == 3
- 0 <= fromi, toi < n
- 1 <= weighti, distanceThreshold <= 10^4

Example:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
"""
def findTheCity(n, edges, distanceThreshold):
    dist = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = dist[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    res, min_count = -1, n+1
    for i in range(n):
        count = sum(dist[i][j] <= distanceThreshold for j in range(n)) - 1
        if count <= min_count:
            min_count = count
            res = i
    return res

# Example usage:
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))  # Output: 3
