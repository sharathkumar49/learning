"""
1219. Path with Maximum Gold

Given a grid of integers, return the maximum amount of gold you can collect by moving up, down, left, or right, starting and ending at any cell with gold.

Constraints:
- 1 <= grid.length, grid[0].length <= 15
- 0 <= grid[i][j] <= 100

Example:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24

"""
def getMaximumGold(grid):
    m, n = len(grid), len(grid[0])
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return 0
        gold = grid[x][y]
        grid[x][y] = 0
        res = 0
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            res = max(res, dfs(x+dx, y+dy))
        grid[x][y] = gold
        return gold + res
    return max(dfs(i, j) for i in range(m) for j in range(n))

# Example usage
if __name__ == "__main__":
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    print(getMaximumGold(grid))  # Output: 24
