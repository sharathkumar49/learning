"""
803. Bricks Falling When Hit

Given a 2D grid of 1s (bricks) and 0s (empty), and a list of hits, return an array representing the number of bricks that will fall after each hit.

Example 1:
Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]

Example 2:
Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 1 <= hits.length <= 4 * 10^4
- grid[i][j] is 0 or 1
- 0 <= hits[i][j] < grid.length or grid[i].length
"""
def hitBricks(grid, hits):
    m, n = len(grid), len(grid[0])
    def neighbors(x, y):
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                yield nx, ny
    for x, y in hits:
        grid[x][y] -= 1
    def dfs(x, y):
        if 0<=x<m and 0<=y<n and grid[x][y]==1:
            grid[x][y]=2
            return 1 + sum(dfs(nx,ny) for nx,ny in neighbors(x,y))
        return 0
    for j in range(n):
        dfs(0, j)
    res = []
    for x, y in reversed(hits):
        grid[x][y] += 1
        if grid[x][y]==1 and any(0<=nx<m and 0<=ny<n and grid[nx][ny]==2 for nx,ny in neighbors(x,y)) or x==0 and grid[x][y]==1:
            res.append(dfs(x,y)-1)
        else:
            res.append(0)
    return res[::-1]

# Example usage:
print(hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]]))  # Output: [2]
print(hitBricks([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]]))  # Output: [0,0]
