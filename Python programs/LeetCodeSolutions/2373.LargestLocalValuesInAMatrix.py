"""
LeetCode 2373. Largest Local Values in a Matrix

Given a matrix, return a matrix of the largest local values in each 3x3 submatrix.

Constraints:
- 1 <= grid.length, grid[0].length <= 100
"""

def largestLocal(grid):
    n = len(grid)
    res = [[0]*(n-2) for _ in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            res[i][j] = max(grid[x][y] for x in range(i,i+3) for y in range(j,j+3))
    return res

# Example usage:
# print(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))  # Output: [[9,9],[8,6]]
