"""
LeetCode 2639. Find the Width of Columns of a Grid

Given a grid, return the width of each column.

Constraints:
- 1 <= grid.length, grid[0].length <= 100
"""

def findColumnWidth(grid):
    return [max(len(str(row[j])) for row in grid) for j in range(len(grid[0]))]
# Example usage:
# print(findColumnWidth([[1,22,333],[44,5,6],[7,8,9]]))  # Output: [2, 2, 3]
