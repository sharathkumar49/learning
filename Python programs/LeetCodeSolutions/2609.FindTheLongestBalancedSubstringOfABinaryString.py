"""
LeetCode 2609. Find the Longest Balanced Substring of a Binary String

Given a binary string, return the length of the longest balanced substring.

Constraints:
- 1 <= s.length <= 50
"""

def findTheLongestBalancedSubstring(s):
    res = 0
    ones = zeros = 0
    i = 0
    n = len(s)
    while i < n:
        zeros = ones = 0
        while i < n and s[i] == '0':
            zeros += 1
            i += 1
        j = i
        while j < n and s[j] == '1':
            ones += 1
            j += 1
        res = max(res, min(zeros, ones)*2)
        i = j
    return res
# Example usage:
# print(findTheLongestBalancedSubstring("01000111"))  # Output: 6
