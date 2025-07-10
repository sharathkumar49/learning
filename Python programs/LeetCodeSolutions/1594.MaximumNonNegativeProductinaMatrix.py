"""
LeetCode 1594. Maximum Non Negative Product in a Matrix

Given a grid of integers, return the maximum non-negative product of a path from the top-left to the bottom-right corner. The product of a path is the product of all the integers along the path. Return -1 if the product is negative.

Example 1:
Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8

Constraints:
- 1 <= grid.length, grid[0].length <= 15
- -4 <= grid[i][j] <= 4
"""

def maxProductPath(grid):
    mod = 10**9 + 7
    m, n = len(grid), len(grid[0])
    dp_max = [[0]*n for _ in range(m)]
    dp_min = [[0]*n for _ in range(m)]
    dp_max[0][0] = dp_min[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            vals = []
            if i > 0:
                vals += [dp_max[i-1][j]*grid[i][j], dp_min[i-1][j]*grid[i][j]]
            if j > 0:
                vals += [dp_max[i][j-1]*grid[i][j], dp_min[i][j-1]*grid[i][j]]
            dp_max[i][j] = max(vals)
            dp_min[i][j] = min(vals)
    return dp_max[-1][-1]%mod if dp_max[-1][-1] >= 0 else -1

# Example usage:
# grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# print(maxProductPath(grid))  # Output: 8
