"""
LeetCode 750. Number Of Corner Rectangles

Given a grid of 0's and 1's, return the number of corner rectangles in the grid.
A corner rectangle is four distinct 1s on the grid that form an axis-aligned rectangle.

Example 1:
Input: grid = [[1,0,0,1,0,1],[0,1,1,0,1,0],[0,0,1,1,1,1],[1,1,1,1,1,1],[0,0,1,1,1,0],[1,0,1,1,1,1]]
Output: 41

Constraints:
- 1 <= grid.length <= 200
- 1 <= grid[0].length <= 200
- 0 <= grid[i][j] <= 1
"""
from typing import List

def countCornerRectangles(grid: List[List[int]]) -> int:
    res = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(i+1, m):
            cnt = 0
            for k in range(n):
                if grid[i][k] and grid[j][k]:
                    cnt += 1
            res += cnt * (cnt - 1) // 2
    return res

# Example usage
if __name__ == "__main__":
    grid = [[1,0,0,1,0,1],[0,1,1,0,1,0],[0,0,1,1,1,1],[1,1,1,1,1,1],[0,0,1,1,1,0],[1,0,1,1,1,1]]
    print(countCornerRectangles(grid))  # Output: 41
