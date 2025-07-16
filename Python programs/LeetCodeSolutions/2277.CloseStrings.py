"""
LeetCode 2277. Close Strings

Given two strings word1 and word2, return true if they are close.

Example:
Input: word1 = "abc", word2 = "bca"
Output: True

Constraints:
- 1 <= word1.length, word2.length <= 10^5
"""

def closeStrings(word1, word2):
    from collections import Counter
    c1, c2 = Counter(word1), Counter(word2)
    return set(word1) == set(word2) and sorted(c1.values()) == sorted(c2.values())

# Example usage:
# print(closeStrings("abc", "bca"))  # Output: True
