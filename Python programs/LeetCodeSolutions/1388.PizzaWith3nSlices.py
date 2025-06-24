"""
LeetCode 1388. Pizza With 3n Slices

You are given a circular pizza with 3n slices labeled from 0 to 3n - 1. Each slice has a different size given in the array slices. You have to pick n slices in such a way that no two picked slices are adjacent (they are not next to each other in the circular pizza), and the sum of the sizes of the slices you pick is as large as possible.

Return the maximum possible sum.

Constraints:
- 1 <= n <= slices.length / 3 <= 100
- slices.length == 3 * n
- 1 <= slices[i] <= 10000

Example:
Input: slices = [1,2,3,4,5,6]
Output: 10
"""
def maxSizeSlices(slices):
    n = len(slices) // 3
    def dp(s):
        m = len(s)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + s[i-1] if i > 1 else 0)
        return dp[m][n]
    return max(dp(slices[1:]), dp(slices[:-1]))

# Example usage:
slices = [1,2,3,4,5,6]
print(maxSizeSlices(slices))  # Output: 10
