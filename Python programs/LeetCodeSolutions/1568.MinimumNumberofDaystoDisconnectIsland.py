"""
LeetCode 1568. Minimum Number of Days to Disconnect Island

Given a 2D grid of 0s and 1s, return the minimum number of days to disconnect the island.

Constraints:
- 1 <= grid.length, grid[0].length <= 30
- grid[i][j] is 0 or 1

Example:
Input: grid = [[1,1],[1,1]]
Output: 2
"""
def minDays(grid):
    m, n = len(grid), len(grid[0])
    def count():
        seen = set()
        def dfs(x, y):
            if 0<=x<m and 0<=y<n and grid[x][y] and (x,y) not in seen:
                seen.add((x,y))
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    dfs(x+dx, y+dy)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in seen:
                    dfs(i,j)
                    cnt += 1
        return cnt
    if count() != 1:
        return 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                grid[i][j] = 0
                if count() != 1:
                    grid[i][j] = 1
                    return 1
                grid[i][j] = 1
    return 2

# Example usage:
grid = [[1,1],[1,1]]
print(minDays(grid))  # Output: 2
