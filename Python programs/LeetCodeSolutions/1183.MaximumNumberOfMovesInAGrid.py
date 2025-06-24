"""
1183. Maximum Number of Moves in a Grid

Given an m x n integer grid, you can start at any cell in the first column and move to the next column by moving right, right-up, or right-down. Return the maximum number of moves you can make.

Constraints:
- 2 <= m, n <= 100
- 1 <= grid[i][j] <= 10^6

Example:
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3

"""
def maxMoves(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    for j in range(n-2, -1, -1):
        for i in range(m):
            for d in [-1, 0, 1]:
                ni = i + d
                if 0 <= ni < m and grid[ni][j+1] > grid[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[ni][j+1])
    return max(dp[i][0] for i in range(m))

# Example usage
if __name__ == "__main__":
    grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
    print(maxMoves(grid))  # Output: 3
