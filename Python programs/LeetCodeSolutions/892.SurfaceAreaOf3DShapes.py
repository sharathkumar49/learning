"""
892. Surface Area of 3D Shapes
https://leetcode.com/problems/surface-area-of-3d-shapes/

You are given an n x n grid where each value v = grid[i][j] represents a tower of v cubes placed on cell (i, j).

After placing these cubes, you have a 3D shape. Return the total surface area of the shape.

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 50
- 0 <= grid[i][j] <= 50

Example:
Input: grid = [[1,2],[3,4]]
Output: 34
Explanation: The surface area is 34.
"""
from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += 2  # top and bottom
                    area += grid[i][j] * 4
                    if i > 0:
                        area -= min(grid[i][j], grid[i-1][j]) * 2
                    if j > 0:
                        area -= min(grid[i][j], grid[i][j-1]) * 2
        return area

# Example usage
if __name__ == "__main__":
    grid = [[1,2],[3,4]]
    print(Solution().surfaceArea(grid))  # Output: 34
