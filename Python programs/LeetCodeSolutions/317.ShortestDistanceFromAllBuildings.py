"""
317. Shortest Distance from All Buildings

You are given an m x n grid of values 0, 1, or 2, where:
- Each 0 marks an empty land that you can pass by freely.
- Each 1 marks a building that you cannot pass through.
- Each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. Return the shortest distance for such a build. If it is not possible, return -1.

Constraints:
- 1 <= m, n <= 50
- grid[i][j] is either 0, 1, or 2
- There will be at least one building in the grid.
"""
from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = [[0]*n for _ in range(m)]
        reach = [[0]*n for _ in range(m)]
        buildings = sum(val == 1 for row in grid for val in row)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited = [[False]*n for _ in range(m)]
                    queue = deque([(i, j, 0)])
                    while queue:
                        x, y, d = queue.popleft()
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                                visited[nx][ny] = True
                                total[nx][ny] += d + 1
                                reach[nx][ny] += 1
                                queue.append((nx, ny, d + 1))
        res = [total[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0 and reach[i][j] == buildings]
        return min(res) if res else -1

# Example usage:
grid = [
  [1,0,2,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]
print(Solution().shortestDistance(grid))  # Output: 7
