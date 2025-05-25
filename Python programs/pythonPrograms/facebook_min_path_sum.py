# Facebook: Find the Minimum Path Sum in a Grid
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# You can only move either down or right at any point in time.

def min_path_sum(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]

if __name__ == "__main__":
    grid1 = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(min_path_sum(grid1))  # Output: 7
    grid2 = [
        [1,2,3],
        [4,5,6]
    ]
    print(min_path_sum(grid2))  # Output: 12
