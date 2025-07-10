"""
LeetCode 1638. Count Substrings That Differ by One Character

Given two strings s and t, return the number of substrings of s and t that differ by exactly one character.

Example 1:
Input: s = "aba", t = "baba"
Output: 6

Constraints:
- 1 <= s.length, t.length <= 100
- s and t consist of lowercase English letters.
"""

def countSubstrings(s, t):
    res = 0
    for i in range(len(s)):
        for j in range(len(t)):
            diff = 0
            k = 0
            while i+k < len(s) and j+k < len(t):
                if s[i+k] != t[j+k]:
                    diff += 1
                if diff > 1:
                    break
                if diff == 1:
                    res += 1
                k += 1
    return res

# Example usage:
# s = "aba"
# t = "baba"
# print(countSubstrings(s, t))  # Output: 6
