"""
LeetCode 1277. Count Square Submatrices with All Ones

Given a m x n matrix of 0s and 1s, return the total number of square submatrices with all ones.

Constraints:
- 1 <= matrix.length <= 300
- 1 <= matrix[0].length <= 300
- 0 <= matrix[i][j] <= 1

Example:
Input: matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
Output: 15
"""
def countSquares(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]:
                if i and j:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                else:
                    dp[i][j] = 1
                res += dp[i][j]
    return res

# Example usage:
matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(countSquares(matrix))  # Output: 15
