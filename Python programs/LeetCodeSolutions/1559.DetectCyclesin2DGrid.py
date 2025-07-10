"""
LeetCode 1559. Detect Cycles in 2D Grid

Given a 2D grid of characters, return true if there is a cycle of the same character in the grid.

Constraints:
- 2 <= grid.length, grid[0].length <= 500
- grid consists of only lowercase English letters.

Example:
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: True
"""
def containsCycle(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    def dfs(x, y, px, py):
        visited[x][y] = True
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==grid[x][y]:
                if not visited[nx][ny]:
                    if dfs(nx, ny, x, y):
                        return True
                elif (nx, ny) != (px, py):
                    return True
        return False
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                if dfs(i, j, -1, -1):
                    return True
    return False

# Example usage:
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
print(containsCycle(grid))  # Output: True
