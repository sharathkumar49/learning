"""
LeetCode 2083. Substrings That Begin and End With the Same Letter

Given a string s, return the number of substrings that begin and end with the same letter.

Example:
Input: s = "abcba"
Output: 7

Constraints:
- 1 <= s.length <= 100
- s consists only of lowercase English letters.
"""

def numberOfSubstrings(s):
    from collections import Counter
    count = Counter(s)
    res = 0
    for v in count.values():
        res += v * (v + 1) // 2
    return res

# Example usage:
# print(numberOfSubstrings("abcba"))  # Output: 7
