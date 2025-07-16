"""
LeetCode 2500. Delete Greatest Value in Each Row

Given a grid, delete the greatest value in each row and return the sum of deleted values.

Constraints:
- 1 <= grid.length, grid[0].length <= 100
"""

def deleteGreatestValue(grid):
    res = 0
    for row in grid:
        res += max(row)
    return res

# Example usage:
# print(deleteGreatestValue([[1,2,4],[3,3,1]]))  # Output: 7
