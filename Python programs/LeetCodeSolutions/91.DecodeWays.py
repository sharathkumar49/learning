"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
Given a string s containing only digits, return the number of ways to decode it.

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zeros.

Example:
Input: s = "12"
Output: 2
"""
def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if i > 1 and '10' <= s[i-2:i] <= '26':
            dp[i] += dp[i-2]
    return dp[n]

# Example usage:
if __name__ == "__main__":
    print(numDecodings("12"))  # Output: 2
    print(numDecodings("226")) # Output: 3
