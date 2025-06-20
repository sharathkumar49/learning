# 62. Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish').
# How many possible unique paths are there?
#
# Example 1:
# Input: m = 3, n = 7
# Output: 28
#
# Example 2:
# Input: m = 3, n = 2
# Output: 3
#
# Constraints:
# 1 <= m, n <= 100

def uniquePaths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

# Example usage
m = 3
n = 7
print("Unique paths:", uniquePaths(m, n))  # Output: 28
