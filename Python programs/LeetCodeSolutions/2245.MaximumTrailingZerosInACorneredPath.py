"""
LeetCode 2245. Maximum Trailing Zeros in a Cornered Path

Given a grid, return the maximum number of trailing zeros in a cornered path.

Example:
Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3

Constraints:
- 2 <= grid.length, grid[0].length <= 100
- 1 <= grid[i][j] <= 10^5
"""

def maxTrailingZeros(grid):
    m, n = len(grid), len(grid[0])
    def count_factors(x, f):
        cnt = 0
        while x % f == 0 and x > 0:
            x //= f
            cnt += 1
        return cnt
    row2 = [[0]*n for _ in range(m)]
    row5 = [[0]*n for _ in range(m)]
    col2 = [[0]*n for _ in range(m)]
    col5 = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            row2[i][j] = count_factors(grid[i][j], 2) + (row2[i][j-1] if j else 0)
            row5[i][j] = count_factors(grid[i][j], 5) + (row5[i][j-1] if j else 0)
    for j in range(n):
        for i in range(m):
            col2[i][j] = count_factors(grid[i][j], 2) + (col2[i-1][j] if i else 0)
            col5[i][j] = count_factors(grid[i][j], 5) + (col5[i-1][j] if i else 0)
    res = 0
    for i in range(m):
        for j in range(n):
            for a, b, c, d in [(row2[i][j], col2[i][j], row5[i][j], col5[i][j])]:
                res = max(res, min(a + b - count_factors(grid[i][j], 2), c + d - count_factors(grid[i][j], 5)))
    return res

# Example usage:
# print(maxTrailingZeros([[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]))  # Output: 3
