"""
LeetCode 1368. Minimum Cost to Make at Least One Valid Path in a Grid

Given a m x n grid with directions (1=right, 2=left, 3=down, 4=up), you can change the direction of a cell at a cost of 1. Return the minimum cost to make a valid path from (0,0) to (m-1,n-1).

Constraints:
- 1 <= m, n <= 100
- grid[i][j] in [1,2,3,4]

Example:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
"""
def minCost(grid):
    from collections import deque
    m, n = len(grid), len(grid[0])
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    dq = deque([(0,0,0)])
    visited = [[float('inf')]*n for _ in range(m)]
    visited[0][0] = 0
    while dq:
        x, y, cost = dq.popleft()
        for d, (dx, dy) in enumerate(dirs):
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                ncost = cost + (grid[x][y] != d+1)
                if ncost < visited[nx][ny]:
                    visited[nx][ny] = ncost
                    if grid[x][y] == d+1:
                        dq.appendleft((nx, ny, ncost))
                    else:
                        dq.append((nx, ny, ncost))
    return visited[m-1][n-1]

# Example usage:
grid = [[1,1,3],[3,2,2],[1,1,4]]
print(minCost(grid))  # Output: 0
