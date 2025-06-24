"""
LeetCode 1416. Restore The Array

Given a string s and an integer k, return the number of ways to split s into a list of integers, each between 1 and k (inclusive), such that the concatenation of the integers is equal to s. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only digits and does not contain leading zeros.
- 1 <= k <= 10^9

Example:
Input: s = "1000", k = 10000
Output: 1
"""
def numberOfArrays(s, k):
    MOD = 10**9+7
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i-1, max(-1, i-10), -1):
            if s[j] == '0': continue
            if int(s[j:i]) <= k:
                dp[i] = (dp[i] + dp[j]) % MOD
    return dp[n]

# Example usage:
s = "1000"
k = 10000
print(numberOfArrays(s, k))  # Output: 1
