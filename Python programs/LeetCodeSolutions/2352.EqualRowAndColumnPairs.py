"""
LeetCode 2352. Equal Row and Column Pairs

Given grid, return the number of equal row and column pairs.

Example:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1

Constraints:
- 1 <= grid.length == grid[0].length <= 200
"""

def equalPairs(grid):
    from collections import Counter
    rows = Counter(tuple(row) for row in grid)
    cols = Counter(tuple(col) for col in zip(*grid))
    return sum(rows[k]*cols[k] for k in rows)

# Example usage:
# print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))  # Output: 1
