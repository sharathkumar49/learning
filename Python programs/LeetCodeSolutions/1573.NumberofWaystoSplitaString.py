"""
LeetCode 1573. Number of Ways to Split a String

Given a binary string s, return the number of ways to split s into three non-empty parts with equal number of 1's. Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- 3 <= s.length <= 10^5
- s consists of '0' and '1'.

Example:
Input: s = "10101"
Output: 4
"""
def numWays(s):
    mod = 10**9 + 7
    ones = s.count('1')
    if ones % 3:
        return 0
    if ones == 0:
        n = len(s) - 1
        return n * (n - 1) // 2 % mod
    k = ones // 3
    first = second = cnt = 0
    for c in s:
        if c == '1':
            cnt += 1
        if cnt == k:
            first += 1
        elif cnt == 2 * k:
            second += 1
    return first * second % mod

# Example usage:
s = "10101"
print(numWays(s))  # Output: 4
