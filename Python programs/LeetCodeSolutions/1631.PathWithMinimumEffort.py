"""
LeetCode 1631. Path With Minimum Effort

Given a 2D grid heights, return the minimum effort required to travel from the top-left to the bottom-right cell. The effort is the maximum absolute difference in heights between two consecutive cells of the path.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2

Constraints:
- 1 <= heights.length, heights[0].length <= 100
- 1 <= heights[i][j] <= 10^6
"""

def minimumEffortPath(heights):
    import heapq
    m, n = len(heights), len(heights[0])
    heap = [(0, 0, 0)]
    dist = [[float('inf')]*n for _ in range(m)]
    dist[0][0] = 0
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    while heap:
        d, x, y = heapq.heappop(heap)
        if x == m-1 and y == n-1:
            return d
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                nd = max(d, abs(heights[x][y] - heights[nx][ny]))
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(heap, (nd, nx, ny))
    return -1

# Example usage:
# heights = [[1,2,2],[3,8,2],[5,3,5]]
# print(minimumEffortPath(heights))  # Output: 2
