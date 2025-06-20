"""
827. Making A Large Island

Given a binary matrix grid, you can change at most one 0 to 1. Return the size of the largest island in the grid after this change.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 500
- grid[i][j] is 0 or 1.
"""
def largestIsland(grid):
    n = len(grid)
    island = [[0]*n for _ in range(n)]
    area = {}
    idx = 2
    def dfs(x, y, idx):
        if 0<=x<n and 0<=y<n and grid[x][y]==1 and island[x][y]==0:
            island[x][y]=idx
            return 1 + sum(dfs(x+dx, y+dy, idx) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)])
        return 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1 and island[i][j]==0:
                area[idx]=dfs(i,j,idx)
                idx+=1
    res = max(area.values() or [0])
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                seen = set()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i+dx, j+dy
                    if 0<=ni<n and 0<=nj<n and island[ni][nj]>1:
                        seen.add(island[ni][nj])
                res = max(res, 1 + sum(area[k] for k in seen))
    return res

# Example usage:
print(largestIsland([[1,0],[0,1]]))  # Output: 3
print(largestIsland([[1,1],[1,0]]))  # Output: 4
