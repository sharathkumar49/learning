"""
LeetCode 1763. Longest Nice Substring

Given a string s, return the longest substring where for every letter, both its uppercase and lowercase appear.

Example 1:
Input: s = "YazaAay"
Output: "aAa"

Constraints:
- 1 <= s.length <= 100
- s consists of uppercase and lowercase English letters
"""

def longestNiceSubstring(s):
    def isNice(sub):
        return set(sub) == set(sub.swapcase())
    n = len(s)
    res = ''
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if len(sub) > len(res) and isNice(sub):
                res = sub
    return res

# Example usage:
# s = "YazaAay"
# print(longestNiceSubstring(s))  # Output: "aAa"
