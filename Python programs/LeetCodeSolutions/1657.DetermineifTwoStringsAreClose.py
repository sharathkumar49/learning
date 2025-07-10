"""
LeetCode 1657. Determine if Two Strings Are Close

Given two strings word1 and word2, return true if you can transform word1 into word2 using any number of operations (swap any two characters, or transform every occurrence of one character into another and vice versa).

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true

Constraints:
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 consist of only lowercase English letters.
"""

def closeStrings(word1, word2):
    from collections import Counter
    c1, c2 = Counter(word1), Counter(word2)
    return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())

# Example usage:
# word1 = "abc"
# word2 = "bca"
# print(closeStrings(word1, word2))  # Output: True
