"""
LeetCode 2093. Minimum Cost to Reach City With Discounts

Given n cities, roads, and discounts, return the minimum cost to reach the last city from the first.

Example:
Input: n = 5, roads = [[0,1,10],[1,2,10],[2,3,10],[3,4,10]], discounts = 2
Output: 20

Constraints:
- 2 <= n <= 10^5
- 1 <= roads.length <= 10^5
"""

def minimumCost(n, roads, discounts):
    import heapq
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    heap = [(0, 0, discounts)]
    dist = [[float('inf')] * (discounts+1) for _ in range(n)]
    dist[0][discounts] = 0
    while heap:
        cost, u, d = heapq.heappop(heap)
        if u == n-1:
            return cost
        if dist[u][d] < cost:
            continue
        for v, w in graph[u]:
            if d > 0 and cost + w//2 < dist[v][d-1]:
                dist[v][d-1] = cost + w//2
                heapq.heappush(heap, (cost + w//2, v, d-1))
            if cost + w < dist[v][d]:
                dist[v][d] = cost + w
                heapq.heappush(heap, (cost + w, v, d))
    return -1

# Example usage:
# print(minimumCost(5, [[0,1,10],[1,2,10],[2,3,10],[3,4,10]], 2))  # Output: 20
