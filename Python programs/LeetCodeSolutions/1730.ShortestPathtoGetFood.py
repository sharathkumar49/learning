"""
LeetCode 1730. Shortest Path to Get Food

Given a grid, find the shortest path from the starting point to the food cell.

Example 1:
Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 200
- grid[i][j] is '*', 'X', 'O', or '#'
"""

def getFood(grid):
    from collections import deque
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                start = (i, j)
    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    while queue:
        x, y, d = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and grid[nx][ny] != 'X':
                if grid[nx][ny] == '#':
                    return d+1
                queue.append((nx,ny,d+1))
                visited.add((nx,ny))
    return -1

# Example usage:
# grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# print(getFood(grid))  # Output: 3
