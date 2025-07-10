"""
LeetCode 2133. Check if Every Row and Column Contains All Numbers

Given a n x n matrix, return true if every row and column contains all numbers from 1 to n.

Example:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- 1 <= matrix[i][j] <= n
"""

def checkValid(matrix):
    n = len(matrix)
    s = set(range(1, n+1))
    for row in matrix:
        if set(row) != s:
            return False
    for col in zip(*matrix):
        if set(col) != s:
            return False
    return True

# Example usage:
# print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))  # Output: True
