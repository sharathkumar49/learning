"""
LeetCode 1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- -100 <= grid[i][j] <= 100

Example:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
"""
def countNegatives(grid):
    m, n = len(grid), len(grid[0])
    res = 0
    for row in grid:
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if row[mid] < 0:
                r = mid
            else:
                l = mid + 1
        res += n - l
    return res

# Example usage:
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))  # Output: 8
