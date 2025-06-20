"""
807. Max Increase to Keep City Skyline

Given a grid of integers representing the height of buildings, return the maximum total sum that the height of the buildings can be increased without changing the city's skyline from any direction.

Example 1:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35

Constraints:
- n == grid.length == grid[i].length
- 2 <= n <= 50
- 0 <= grid[i][j] <= 100
"""
def maxIncreaseKeepingSkyline(grid):
    n = len(grid)
    row_max = [max(row) for row in grid]
    col_max = [max(col) for col in zip(*grid)]
    return sum(min(row_max[i], col_max[j]) - grid[i][j] for i in range(n) for j in range(n))

# Example usage:
print(maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))  # Output: 35
