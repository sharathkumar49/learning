"""
LeetCode 1293. Shortest Path in a Grid with Obstacles Elimination

Given a m x n grid where each cell is either 0 (empty) or 1 (obstacle), and an integer k, return the shortest path from (0,0) to (m-1,n-1) that eliminates at most k obstacles. If not possible, return -1.

Constraints:
- 1 <= m, n <= 40
- 0 <= k <= m*n
- grid[i][j] is 0 or 1

Example:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
"""
def shortestPath(grid, k):
    from collections import deque
    m, n = len(grid), len(grid[0])
    queue = deque([(0, 0, k, 0)])
    seen = dict()
    while queue:
        x, y, rem, steps = queue.popleft()
        if (x, y) == (m-1, n-1):
            return steps
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                nrem = rem - grid[nx][ny]
                if nrem >= 0 and ((nx,ny) not in seen or seen[(nx,ny)] < nrem):
                    seen[(nx,ny)] = nrem
                    queue.append((nx, ny, nrem, steps+1))
    return -1

# Example usage:
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
print(shortestPath(grid, k))  # Output: 6
