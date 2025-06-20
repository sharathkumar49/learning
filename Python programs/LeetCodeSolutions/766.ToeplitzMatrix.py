"""
766. Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation: In the above grid, the diagonals are:
"""
# [9]
# [5, 5]
# [1, 1, 1]
# [2, 2, 2]
# [3, 3]
# [4]
# All diagonals from top-left to bottom-right have the same elements.
"""

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 20
- 0 <= matrix[i][j] <= 99

"""

def isToeplitzMatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] != matrix[r-1][c-1]:
                return False
    return True

# Example usage:
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(isToeplitzMatrix(matrix))  # Output: True
