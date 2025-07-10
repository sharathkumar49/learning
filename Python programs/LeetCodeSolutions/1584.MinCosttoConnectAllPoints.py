"""
LeetCode 1584. Min Cost to Connect All Points

Given an array points representing integer coordinates of some points on a 2D-plane, return the minimum cost to make all points connected. The cost is the Manhattan distance between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Constraints:
- 1 <= points.length <= 1000
- -10^6 <= points[i][0], points[i][1] <= 10^6
"""

def minCostConnectPoints(points):
    import heapq
    n = len(points)
    visited = set()
    minHeap = [(0, 0)]
    res = 0
    while len(visited) < n:
        cost, u = heapq.heappop(minHeap)
        if u in visited:
            continue
        res += cost
        visited.add(u)
        for v in range(n):
            if v not in visited:
                d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(minHeap, (d, v))
    return res

# Example usage:
# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# print(minCostConnectPoints(points))  # Output: 20
