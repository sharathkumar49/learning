"""
LeetCode 2414. Length of the Longest Alphabetical Continuous Substring

Given a string, return the length of the longest alphabetical continuous substring.

Constraints:
- 1 <= s.length <= 10^5
"""

def longestContinuousSubstring(s):
    res = cur = 1
    for i in range(1, len(s)):
        if ord(s[i]) == ord(s[i-1])+1:
            cur += 1
        else:
            cur = 1
        res = max(res, cur)
    return res

# Example usage:
# print(longestContinuousSubstring("abacaba"))  # Output: 2
