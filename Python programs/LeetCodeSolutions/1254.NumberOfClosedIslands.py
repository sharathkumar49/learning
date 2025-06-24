"""
1254. Number of Closed Islands

Given a 2D grid, return the number of closed islands. A closed island is surrounded by water on all sides.

Constraints:
- 1 <= grid.length, grid[0].length <= 100
- grid[i][j] is 0 (land) or 1 (water)

Example:
Input: grid = [[1,1,1,1,0,1,1,1],[1,0,0,1,0,1,0,1],[1,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,1]]
Output: 2

"""
def closedIsland(grid):
    m, n = len(grid), len(grid[0])
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if grid[x][y] == 1:
            return True
        grid[x][y] = 1
        up = dfs(x-1, y)
        down = dfs(x+1, y)
        left = dfs(x, y-1)
        right = dfs(x, y+1)
        return up and down and left and right
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and dfs(i, j):
                count += 1
    return count

# Example usage
if __name__ == "__main__":
    grid = [[1,1,1,1,0,1,1,1],[1,0,0,1,0,1,0,1],[1,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,1]]
    print(closedIsland(grid))  # Output: 2
