"""
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path from top-left to bottom-right. If no such path exists, return -1.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Example:
Input: grid = [[0,1],[1,0]]
Output: 2
"""
from typing import List
from collections import deque

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    queue = deque([(0, 0, 1)])
    visited = set([(0, 0)])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while queue:
        x, y, d = queue.popleft()
        if (x, y) == (n-1, n-1):
            return d
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, d+1))
    return -1

# Example usage:
grid = [[0,1],[1,0]]
print(shortestPathBinaryMatrix(grid))  # Output: 2
