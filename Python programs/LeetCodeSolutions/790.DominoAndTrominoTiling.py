"""
790. Domino and Tromino Tiling

You have a 2 x n board. You can tile the board with dominoes (2x1 or 1x2) and trominoes (L-shaped). Return the number of ways to tile the board modulo 10^9 + 7.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
- 1 <= n <= 1000
"""
def numTilings(n):
    MOD = 10**9 + 7
    dp = [0] * (n+3)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (2*dp[i-1] + dp[i-3]) % MOD
    return dp[n]

# Example usage:
print(numTilings(3))  # Output: 5
print(numTilings(1))  # Output: 1
