"""
LeetCode 1380. Lucky Numbers in a Matrix

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 50
- 1 <= matrix[i][j] <= 10^5
- All elements in the matrix are distinct.

Example:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
"""
def luckyNumbers (matrix):
    min_row = set(min(row) for row in matrix)
    max_col = set(max(col) for col in zip(*matrix))
    return list(min_row & max_col)

# Example usage:
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(matrix))  # Output: [15]
