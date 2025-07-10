"""
LeetCode 1513. Number of Substrings With Only 1s

Given a binary string s, return the number of substrings with only 1s. Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.

Example:
Input: s = "0110111"
Output: 9
"""
def numSub(s):
    mod = 10**9 + 7
    res = count = 0
    for c in s:
        if c == '1':
            count += 1
        else:
            res += count * (count + 1) // 2
            count = 0
    res += count * (count + 1) // 2
    return res % mod

# Example usage:
s = "0110111"
print(numSub(s))  # Output: 9
