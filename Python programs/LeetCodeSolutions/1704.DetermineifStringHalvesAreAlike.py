"""
LeetCode 1704. Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two halves of equal lengths, and determine if both halves are alike. Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', case-insensitive).

Example 1:
Input: s = "book"
Output: true
Explanation: "bo" and "ok". Both halves contain 1 vowel.

Constraints:
- 2 <= s.length <= 1000
- s.length is even
- s consists of uppercase and lowercase letters
"""

def halvesAreAlike(s):
    vowels = set('aeiouAEIOU')
    n = len(s) // 2
    return sum(c in vowels for c in s[:n]) == sum(c in vowels for c in s[n:])

# Example usage:
# s = "book"
# print(halvesAreAlike(s))  # Output: True
