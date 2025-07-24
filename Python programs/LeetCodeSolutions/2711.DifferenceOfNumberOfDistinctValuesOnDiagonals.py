"""
LeetCode 2711. Difference of Number of Distinct Values on Diagonals

Given grid, return the difference of number of distinct values on diagonals for each cell.

Constraints:
- 1 <= grid.length, grid[0].length <= 50
"""

def differenceOfDistinctValues(grid):
    m, n = len(grid), len(grid[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            s1, s2 = set(), set()
            x, y = i-1, j-1
            while x >= 0 and y >= 0:
                s1.add(grid[x][y])
                x -= 1
                y -= 1
            x, y = i+1, j+1
            while x < m and y < n:
                s2.add(grid[x][y])
                x += 1
                y += 1
            res[i][j] = abs(len(s1) - len(s2))
    return res
# Example usage:
# print(differenceOfDistinctValues([[1,2,3],[3,1,5],[3,2,1]]))  # Output: [[1,1,0],[1,0,1],[0,1,1]]
