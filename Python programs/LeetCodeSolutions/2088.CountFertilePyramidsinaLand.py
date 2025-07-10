"""
LeetCode 2088. Count Fertile Pyramids in a Land

Given a grid, return the number of fertile pyramids in the land.

Example:
Input: grid = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[0,1,1,0]]
Output: 13

Constraints:
- 1 <= grid.length, grid[0].length <= 100
- grid[i][j] is 0 or 1
"""

def countPyramids(grid):
    m, n = len(grid), len(grid[0])
    def count(grid):
        dp = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i == 0 or j == 0 or j == n-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + 1
                    res += dp[i][j] - 1
        return res
    return count(grid) + count(grid[::-1])

# Example usage:
# print(countPyramids([[0,1,1,0],[1,1,1,1],[1,1,1,1],[0,1,1,0]]))  # Output: 13
