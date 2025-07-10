"""
LeetCode 2002. Maximum Product of the Length of Two Palindromic Subsequences

Given a string s, split it into two disjoint subsequences such that both are palindromic. Return the maximum product of their lengths.

Example:
Input: s = "leetcodecom"
Output: 9

Constraints:
- 2 <= s.length <= 12
- s consists only of lowercase English letters.
"""

def maxProduct(s):
    def is_palindrome(x):
        return x == x[::-1]
    n = len(s)
    res = 0
    for mask in range(1, 1 << n):
        a = ''.join(s[i] for i in range(n) if mask & (1 << i))
        b = ''.join(s[i] for i in range(n) if not (mask & (1 << i)))
        if is_palindrome(a) and is_palindrome(b):
            res = max(res, len(a) * len(b))
    return res

# Example usage:
# print(maxProduct("leetcodecom"))  # Output: 9
