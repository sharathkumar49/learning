"""
LeetCode 1641. Count Sorted Vowel Strings

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

Example 1:
Input: n = 2
Output: 15

Constraints:
- 1 <= n <= 50
"""

def countVowelStrings(n):
    from math import comb
    return comb(n+4, 4)

# Example usage:
# n = 2
# print(countVowelStrings(n))  # Output: 15
