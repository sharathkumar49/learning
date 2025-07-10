"""
LeetCode 1930. Unique Length-3 Palindromic Subsequences

Given a string s, return the number of unique palindromic subsequences of length 3.

Example:
Input: s = "aabca"
Output: 3

Constraints:
- 3 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

def countPalindromicSubsequence(s):
    res = set()
    for c in set(s):
        i, j = s.find(c), s.rfind(c)
        if i < j:
            res |= set(s[i+1:j])
    return len(res)

# Example usage:
# print(countPalindromicSubsequence("aabca"))  # Output: 3
