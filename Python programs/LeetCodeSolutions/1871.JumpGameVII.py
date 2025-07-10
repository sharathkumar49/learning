"""
LeetCode 1871. Jump Game VII

You are given a binary string s and two integers minJump and maxJump. Return true if you can reach the last index starting from the first index, otherwise false.

Example:
Input: s = "011010", minJump = 2, maxJump = 3
Output: true

Constraints:
- 2 <= s.length <= 10^5
- s[i] is either '0' or '1'.
- 1 <= minJump <= maxJump < s.length
"""

def canReach(s, minJump, maxJump):
    n = len(s)
    dp = [False] * n
    dp[0] = True
    pre = 0
    for i in range(1, n):
        if i >= minJump:
            pre += dp[i - minJump]
        if i > maxJump:
            pre -= dp[i - maxJump - 1]
        dp[i] = s[i] == '0' and pre > 0
    return dp[-1]

# Example usage:
# print(canReach("011010", 2, 3))  # Output: True
