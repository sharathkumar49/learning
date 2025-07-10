"""
LeetCode 1878. Get Biggest Three Rhombus Sums in a Grid

Given an m x n integer grid, return the biggest three distinct rhombus sums in the grid as a sorted list in descending order.

Example:
Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,1]]
Output: [228,216,211]

Constraints:
- 1 <= m, n <= 50
- 1 <= grid[i][j] <= 10^5
"""

def getBiggestThree(grid):
    m, n = len(grid), len(grid[0])
    res = set()
    for i in range(m):
        for j in range(n):
            res.add(grid[i][j])
            for k in range(1, min(m, n)):
                if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                    break
                s = 0
                for d in range(k):
                    s += grid[i-d][j+d] + grid[i-d][j-d] + grid[i+d][j+d] + grid[i+d][j-d]
                s += grid[i-k][j] + grid[i+k][j] + grid[i][j-k] + grid[i][j+k]
                s -= grid[i][j]*3
                res.add(s)
    return sorted(res, reverse=True)[:3]

# Example usage:
# print(getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,1]]))  # Output: [228,216,211]
