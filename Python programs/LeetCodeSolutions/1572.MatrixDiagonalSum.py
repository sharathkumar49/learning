"""
LeetCode 1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Constraints:
- n == mat.length == mat[i].length
- 1 <= n <= 100
- 1 <= mat[i][j] <= 100

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: 25
"""
def diagonalSum(mat):
    n = len(mat)
    res = 0
    for i in range(n):
        res += mat[i][i] + mat[i][n-1-i]
    if n % 2:
        res -= mat[n//2][n//2]
    return res

# Example usage:
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))  # Output: 25
