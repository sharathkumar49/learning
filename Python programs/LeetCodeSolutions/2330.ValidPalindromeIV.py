"""
LeetCode 2330. Valid Palindrome IV

Given s, return true if s can be rearranged to form a palindrome.

Example:
Input: s = "aabb"
Output: True

Constraints:
- 1 <= s.length <= 1000
"""

def canFormPalindrome(s):
    from collections import Counter
    c = Counter(s)
    return sum(v%2 for v in c.values()) <= 1

# Example usage:
# print(canFormPalindrome("aabb"))  # Output: True
