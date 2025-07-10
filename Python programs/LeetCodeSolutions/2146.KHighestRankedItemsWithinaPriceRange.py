"""
LeetCode 2146. K Highest Ranked Items Within a Price Range

You are given a 2D grid of integers representing a store, where grid[i][j] is the price of the item at (i, j). You are also given pricing = [low, high], start = [row, col], and k. Return the positions of the k highest ranked items within the price range, sorted by distance from start, then by price, then by row, then by column.

Example:
Input: grid = [[1,2,3],[2,3,4],[3,4,5]], pricing = [2,3], start = [0,0], k = 3
Output: [[0,1],[1,0],[1,1]]

Constraints:
- 1 <= grid.length, grid[0].length <= 100
- 1 <= grid[i][j] <= 10^5
- 1 <= k <= grid.length * grid[0].length
"""

from collections import deque

def highestRankedKItems(grid, pricing, start, k):
    m, n = len(grid), len(grid[0])
    low, high = pricing
    visited = [[False]*n for _ in range(m)]
    res = []
    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    while q:
        x, y, dist = q.popleft()
        if low <= grid[x][y] <= high:
            res.append((dist, grid[x][y], x, y))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]!=0:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))
    res.sort()
    return [[x, y] for _,_,x,y in res[:k]]

# Example usage:
# print(highestRankedKItems([[1,2,3],[2,3,4],[3,4,5]], [2,3], [0,0], 3))  # Output: [[0,1],[1,0],[1,1]]
