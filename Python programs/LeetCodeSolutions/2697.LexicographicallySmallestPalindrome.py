"""
LeetCode 2697. Lexicographically Smallest Palindrome

Given s, return the lexicographically smallest palindrome.

Constraints:
- 1 <= s.length <= 100
"""

def makeSmallestPalindrome(s):
    s = list(s)
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            m = min(s[i], s[n-1-i])
            s[i] = s[n-1-i] = m
    return ''.join(s)
# Example usage:
# print(makeSmallestPalindrome("egcfe"))  # Output: "efcfe"
