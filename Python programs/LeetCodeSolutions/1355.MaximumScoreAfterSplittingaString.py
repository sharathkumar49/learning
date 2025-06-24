"""
LeetCode 1355. Maximum Score After Splitting a String

Given a string s of 0s and 1s, split it into two non-empty substrings, and return the maximum score (number of 0s in the left + number of 1s in the right).

Constraints:
- 2 <= s.length <= 500
- s consists of '0' and '1' only.

Example:
Input: s = "011101"
Output: 5
"""
def maxScore(s):
    res = 0
    for i in range(1, len(s)):
        res = max(res, s[:i].count('0') + s[i:].count('1'))
    return res

# Example usage:
s = "011101"
print(maxScore(s))  # Output: 5
