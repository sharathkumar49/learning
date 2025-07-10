"""
LeetCode 1928. Minimum Cost to Reach Destination in Time

Given an array edges, an integer maxTime, and an array passingFees, return the minimum cost to reach the destination within maxTime.

Example:
Input: edges = [[0,1,10],[1,2,10],[0,2,30]], maxTime = 20, passingFees = [1,2,3]
Output: 3

Constraints:
- 2 <= n <= 1000
- 1 <= edges.length <= 10000
- 0 <= edges[i][0], edges[i][1] < n
- 1 <= edges[i][2] <= 1000
- 1 <= maxTime <= 1000
- 1 <= passingFees[i] <= 1000
"""

import heapq

def minCost(maxTime, edges, passingFees):
    n = len(passingFees)
    graph = [[] for _ in range(n)]
    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))
    dp = [ [float('inf')] * (maxTime+1) for _ in range(n)]
    dp[0][0] = passingFees[0]
    hq = [(passingFees[0], 0, 0)]
    while hq:
        cost, u, time = heapq.heappop(hq)
        if u == n-1:
            return cost
        for v, t in graph[u]:
            if time + t <= maxTime and cost + passingFees[v] < dp[v][time+t]:
                dp[v][time+t] = cost + passingFees[v]
                heapq.heappush(hq, (dp[v][time+t], v, time+t))
    return -1

# Example usage:
# print(minCost(20, [[0,1,10],[1,2,10],[0,2,30]], [1,2,3]))  # Output: 3
