"""
LeetCode 2428. Maximum Sum of an Hourglass

Given a grid, return the maximum sum of an hourglass.

Constraints:
- 3 <= grid.length, grid[0].length <= 100
"""

def maxSum(grid):
    m, n = len(grid), len(grid[0])
    res = float('-inf')
    for i in range(m-2):
        for j in range(n-2):
            s = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
            res = max(res, s)
    return res

# Example usage:
# print(maxSum([[6,2,1,3],[4,2,1,5],[1,1,1,1],[2,4,1,2]]))  # Output: 19
