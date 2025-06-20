"""
639. Decode Ways II
Difficulty: Hard

A message containing letters from A-Z can be encoded into numbers using the mapping 'A'->1, 'B'->2, ..., 'Z'->26. Now, '*' can represent any digit from '1' to '9'. Return the total number of ways to decode the message, modulo 10^9 + 7.

Example 1:
Input: s = "*"
Output: 9

Example 2:
Input: s = "1*"
Output: 18

Constraints:
1 <= s.length <= 10^5
s consists of digits and '*' characters.
"""

def numDecodings(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [1, 0, 0]
    for i in range(n):
        dp2 = [0, 0, 0]
        if s[i] == '*':
            dp2[0] = 9 * dp[0]
        elif s[i] != '0':
            dp2[0] = dp[0]
        if i > 0:
            if s[i-1] == '*' and s[i] == '*':
                dp2[0] += 15 * dp[1]
            elif s[i-1] == '*':
                dp2[0] += (2 if s[i] <= '6' else 1) * dp[1]
            elif s[i] == '*':
                dp2[0] += (9 if s[i-1] == '1' else 6 if s[i-1] == '2' else 0) * dp[1]
            elif 10 <= int(s[i-1:i+1]) <= 26:
                dp2[0] += dp[1]
        dp2[0] %= MOD
        dp = [dp2[0], dp[0], dp[1]]
    return dp[0]

# Example usage
if __name__ == "__main__":
    print(numDecodings("*"))   # Output: 9
    print(numDecodings("1*"))  # Output: 18
