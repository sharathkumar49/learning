"""
867. Transpose Matrix

Given a 2D integer array matrix, return the transpose of the matrix.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
- 1 <= matrix.length, matrix[i].length <= 1000
- 1 <= matrix[i][j] <= 10^9
"""
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Example usage:
print(transpose([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [[1,4,7],[2,5,8],[3,6,9]]
print(transpose([[1,2,3],[4,5,6]]))          # Output: [[1,4],[2,5],[3,6]]
