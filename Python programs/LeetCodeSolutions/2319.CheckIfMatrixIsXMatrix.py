"""
LeetCode 2319. Check if Matrix Is X-Matrix

Given grid, return true if it is an X-matrix.

Example:
Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
Output: True

Constraints:
- 3 <= grid.length == grid[0].length <= 100
"""

def checkXMatrix(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True

# Example usage:
# print(checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))  # Output: True
