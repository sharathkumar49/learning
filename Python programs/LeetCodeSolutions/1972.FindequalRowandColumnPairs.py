"""
LeetCode 1972. Find Equal Row and Column Pairs

Given a square matrix grid, return the number of pairs (r, c) such that row r and column c are equal.

Example:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 200
- 1 <= grid[i][j] <= 10^5
"""

def equalPairs(grid):
    n = len(grid)
    rows = [tuple(row) for row in grid]
    cols = [tuple(grid[i][j] for i in range(n)) for j in range(n)]
    from collections import Counter
    return sum(Counter(rows)[col] for col in cols)

# Example usage:
# print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))  # Output: 1
