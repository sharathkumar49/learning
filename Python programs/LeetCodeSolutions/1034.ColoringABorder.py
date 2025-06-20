"""
1034. Coloring A Border

Given a 2D grid of integers, a starting cell (r0, c0), and a color, color the border of the connected component containing (r0, c0) with the given color.

Constraints:
- 1 <= grid.length, grid[0].length <= 50
- 0 <= grid[i][j], color <= 1000
- 0 <= r0 < grid.length
- 0 <= c0 < grid[0].length

Example:
Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3,3],[3,2]]
"""
from typing import List

def colorBorder(grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    orig = grid[r0][c0]
    visited = [[False]*n for _ in range(m)]
    borders = []
    def dfs(i, j):
        visited[i][j] = True
        is_border = False
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= x < m and 0 <= y < n:
                if not visited[x][y] and grid[x][y] == orig:
                    dfs(x, y)
                elif grid[x][y] != orig:
                    is_border = True
            else:
                is_border = True
        if is_border:
            borders.append((i, j))
    dfs(r0, c0)
    for i, j in borders:
        grid[i][j] = color
    return grid

# Example usage:
grid = [[1,1],[1,2]]
r0, c0, color = 0, 0, 3
print(colorBorder(grid, r0, c0, color))  # Output: [[3, 3], [3, 2]]
