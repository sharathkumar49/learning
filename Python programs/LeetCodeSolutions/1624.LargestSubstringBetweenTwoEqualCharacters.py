"""
LeetCode 1624. Largest Substring Between Two Equal Characters

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring, return -1.

Example 1:
Input: s = "aa"
Output: 0

Constraints:
- 1 <= s.length <= 300
- s consists of only lowercase English letters.
"""

def maxLengthBetweenEqualCharacters(s):
    pos = {}
    res = -1
    for i, c in enumerate(s):
        if c in pos:
            res = max(res, i - pos[c] - 1)
        else:
            pos[c] = i
    return res

# Example usage:
# s = "aa"
# print(maxLengthBetweenEqualCharacters(s))  # Output: 0
