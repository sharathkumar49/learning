"""
562. Longest Line of Consecutive One in Matrix
Difficulty: Medium

Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal, or anti-diagonal.

Example 1:
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3

Constraints:
1 <= m, n <= 200
mat[i][j] is either 0 or 1.
"""

def longestLine(mat):
    if not mat or not mat[0]:
        return 0
    m, n = len(mat), len(mat[0])
    res = 0
    dp = [[[0]*4 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                dp[i][j][0] = (dp[i-1][j][0] if i > 0 else 0) + 1  # vertical
                dp[i][j][1] = (dp[i][j-1][1] if j > 0 else 0) + 1  # horizontal
                dp[i][j][2] = (dp[i-1][j-1][2] if i > 0 and j > 0 else 0) + 1  # diagonal
                dp[i][j][3] = (dp[i-1][j+1][3] if i > 0 and j < n-1 else 0) + 1  # anti-diagonal
                res = max(res, max(dp[i][j]))
    return res

# Example usage
if __name__ == "__main__":
    print(longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))  # Output: 3
