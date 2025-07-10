"""
LeetCode 1975. Maximum Matrix Sum

Given a matrix, return the maximum sum of the matrix after flipping the sign of any number of elements.

Example:
Input: matrix = [[1,-1],[-1,1]]
Output: 4

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 70
- -10^6 <= matrix[i][j] <= 10^6
"""

def maxMatrixSum(matrix):
    total = 0
    min_abs = float('inf')
    neg = 0
    for row in matrix:
        for x in row:
            total += abs(x)
            min_abs = min(min_abs, abs(x))
            if x < 0:
                neg += 1
    if neg % 2:
        total -= 2 * min_abs
    return total

# Example usage:
# print(maxMatrixSum([[1,-1],[-1,1]]))  # Output: 4
