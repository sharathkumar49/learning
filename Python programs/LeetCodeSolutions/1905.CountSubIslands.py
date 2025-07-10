"""
LeetCode 1905. Count Sub Islands

Given two m x n binary matrices grid1 and grid2, return the number of sub-islands in grid2. A sub-island is an island in grid2 that is also an island in grid1.

Example:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3

Constraints:
- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 500
- grid1[i][j], grid2[i][j] is 0 or 1
"""

def countSubIslands(grid1, grid2):
    m, n = len(grid1), len(grid1[0])
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] != 1:
            return True
        grid2[i][j] = -1
        res = grid1[i][j] == 1
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            res = dfs(i+dx, j+dy) and res
        return res
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 1 and dfs(i, j):
                ans += 1
    return ans

# Example usage:
# print(countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))  # Output: 3
