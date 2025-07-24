"""
LeetCode 2728. Find the Longest Semi-Repetitive Substring

Given s, return the length of the longest semi-repetitive substring.

Constraints:
- 1 <= s.length <= 100
"""

def longestSemiRepetitiveSubstring(s):
    res = cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt = 1
        else:
            cnt += 1
        res = max(res, cnt)
    return res
# Example usage:
# print(longestSemiRepetitiveSubstring("52233"))  # Output: 4
