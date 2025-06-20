"""
629. K Inverse Pairs Array
Difficulty: Hard

Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1

Example 2:
Input: n = 3, k = 1
Output: 2

Constraints:
1 <= n <= 1000
0 <= k <= 1000
"""

def kInversePairs(n, k):
    MOD = 10**9 + 7
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(1, k+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
            if j >= i:
                dp[i][j] = (dp[i][j] - dp[i-1][j-i] + MOD) % MOD
    return dp[n][k]

# Example usage
if __name__ == "__main__":
    print(kInversePairs(3, 0))  # Output: 1
    print(kInversePairs(3, 1))  # Output: 2
