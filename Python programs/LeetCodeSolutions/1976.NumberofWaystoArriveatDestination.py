"""
LeetCode 1976. Number of Ways to Arrive at Destination

Given a weighted undirected graph, return the number of ways to arrive at the destination in the shortest time.

Example:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]], start = 0, end = 6
Output: 4

Constraints:
- 1 <= n <= 200
- 1 <= roads.length <= n * (n - 1) / 2
- 0 <= u, v <= n-1
- 1 <= time <= 10^9
"""

def countPaths(n, roads):
    import heapq
    MOD = 10**9+7
    graph = [[] for _ in range(n)]
    for u, v, t in roads:
        graph[u].append((v, t))
        graph[v].append((u, t))
    dist = [float('inf')]*n
    ways = [0]*n
    dist[0] = 0
    ways[0] = 1
    hq = [(0, 0)]
    while hq:
        d, u = heapq.heappop(hq)
        if d > dist[u]: continue
        for v, t in graph[u]:
            if d + t < dist[v]:
                dist[v] = d + t
                ways[v] = ways[u]
                heapq.heappush(hq, (dist[v], v))
            elif d + t == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD
    return ways[n-1]

# Example usage:
# print(countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))  # Output: 4
