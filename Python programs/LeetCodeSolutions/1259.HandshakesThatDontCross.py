"""
1259. Handshakes That Don't Cross

Given n people sitting in a circle, return the number of ways they can shake hands so that no two handshakes cross. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 1000
- n is even

Example:
Input: n = 4
Output: 2

"""
def numberOfWays(n):
    MOD = 10**9 + 7
    dp = [1] + [0]*n
    for i in range(2, n+1, 2):
        for j in range(0, i, 2):
            dp[i] = (dp[i] + dp[j] * dp[i-2-j]) % MOD
    return dp[n]

# Example usage
if __name__ == "__main__":
    print(numberOfWays(4))  # Output: 2
