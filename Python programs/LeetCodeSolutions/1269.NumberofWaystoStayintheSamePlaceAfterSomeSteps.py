"""
LeetCode 1269. Number of Ways to Stay in the Same Place After Some Steps

You have a pointer at index 0 in an array of length arrLen. At each step, you can move left, right, or stay in the same place (as long as you stay within the array bounds). Return the number of ways to stay at index 0 after exactly steps steps. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= steps <= 500
- 1 <= arrLen <= 10^6

Example:
Input: steps = 3, arrLen = 2
Output: 4
"""
def numWays(steps, arrLen):
    MOD = 10**9 + 7
    max_pos = min(steps//2+1, arrLen)
    dp = [0] * max_pos
    dp[0] = 1
    for _ in range(steps):
        ndp = [0] * max_pos
        for i in range(max_pos):
            ndp[i] = dp[i]
            if i > 0:
                ndp[i] = (ndp[i] + dp[i-1]) % MOD
            if i < max_pos-1:
                ndp[i] = (ndp[i] + dp[i+1]) % MOD
        dp = ndp
    return dp[0]

# Example usage:
print(numWays(3, 2))  # Output: 4
