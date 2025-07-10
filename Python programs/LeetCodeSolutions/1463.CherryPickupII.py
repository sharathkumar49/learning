"""
LeetCode 1463. Cherry Pickup II

Given a rows x cols matrix grid representing the number of cherries in each cell, two robots start at the top row and can move to the next row, picking cherries. Return the maximum number of cherries both robots can collect.

Constraints:
- 2 <= rows, cols <= 70
- 0 <= grid[i][j] <= 100

Example:
Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
"""
def cherryPickup(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[[0]*cols for _ in range(cols)] for _ in range(rows)]
    for c1 in range(cols):
        for c2 in range(cols):
            if c1 == c2:
                dp[rows-1][c1][c2] = grid[rows-1][c1]
            else:
                dp[rows-1][c1][c2] = grid[rows-1][c1] + grid[rows-1][c2]
    for r in range(rows-2, -1, -1):
        for c1 in range(cols):
            for c2 in range(cols):
                for dc1 in [-1,0,1]:
                    for dc2 in [-1,0,1]:
                        nc1, nc2 = c1+dc1, c2+dc2
                        if 0 <= nc1 < cols and 0 <= nc2 < cols:
                            val = dp[r+1][nc1][nc2]
                            if c1 == c2:
                                val += grid[r][c1]
                            else:
                                val += grid[r][c1] + grid[r][c2]
                            dp[r][c1][c2] = max(dp[r][c1][c2], val)
    return dp[0][0][cols-1]

# Example usage:
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(cherryPickup(grid))  # Output: 24
