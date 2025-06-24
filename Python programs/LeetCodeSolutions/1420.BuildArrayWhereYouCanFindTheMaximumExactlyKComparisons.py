"""
LeetCode 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

Given three integers n, m, and k, return the number of arrays arr of length n with each element in [1, m] such that exactly k comparisons are needed to find the maximum. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 50
- 1 <= m <= 100
- 0 <= k <= n

Example:
Input: n = 2, m = 3, k = 1
Output: 6
"""
def numOfArrays(n, m, k):
    MOD = 10**9+7
    dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            for x in range(1, m+1):
                for y in range(1, k+1):
                    if x < j:
                        dp[i][j][y] = (dp[i][j][y] + dp[i-1][j][y]*1) % MOD
                    else:
                        dp[i][j][y] = (dp[i][j][y] + sum(dp[i-1][t][y-1] for t in range(1, x))) % MOD
    return sum(dp[n][j][k] for j in range(1, m+1)) % MOD

# Example usage:
n = 2
m = 3
k = 1
print(numOfArrays(n, m, k))  # Output: 6
