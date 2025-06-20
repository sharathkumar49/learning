"""
883. Projection Area of 3D Shapes

You are given an n x n grid where grid[i][j] represents the height of a stack of cubes. Return the total projection area.

Example 1:
Input: grid = [[1,2],[3,4]]
Output: 17

Example 2:
Input: grid = [[2]]
Output: 5

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 50
- 0 <= grid[i][j] <= 50
"""
def projectionArea(grid):
    n = len(grid)
    xy = sum(v > 0 for row in grid for v in row)
    yz = sum(max(row) for row in grid)
    zx = sum(max(col) for col in zip(*grid))
    return xy + yz + zx

# Example usage:
print(projectionArea([[1,2],[3,4]]))  # Output: 17
print(projectionArea([[2]]))          # Output: 5
