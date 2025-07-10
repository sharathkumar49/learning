"""
LeetCode 1888. Minimum Number of Flips to Make the Binary String Alternating

Given a binary string s, return the minimum number of flips to make s alternating, considering all rotations of s.

Example:
Input: s = "111000"
Output: 2

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

def minFlips(s):
    n = len(s)
    s = s + s
    alt1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(2*n)])
    alt2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(2*n)])
    res = n
    diff1 = diff2 = 0
    for i in range(2*n):
        if s[i] != alt1[i]: diff1 += 1
        if s[i] != alt2[i]: diff2 += 1
        if i >= n:
            if s[i-n] != alt1[i-n]: diff1 -= 1
            if s[i-n] != alt2[i-n]: diff2 -= 1
        if i >= n-1:
            res = min(res, diff1, diff2)
    return res

# Example usage:
# print(minFlips("111000"))  # Output: 2
