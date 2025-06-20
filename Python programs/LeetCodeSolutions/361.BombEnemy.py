"""
361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E', or empty '0'. Return the maximum enemies you can kill using one bomb. The bomb kills all enemies in the same row and column until it hits a wall.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid[i][j] is 'W', 'E', or '0'.
"""
from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = row_hits = 0
        col_hits = [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    row_hits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_hits += 1
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_hits[j] += 1
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, row_hits + col_hits[j])
        return res

# Example usage:
grid = [
  ["0","E","0","0"],
  ["E","0","W","E"],
  ["0","E","0","0"]
]
print(Solution().maxKilledEnemies(grid))  # Output: 3
