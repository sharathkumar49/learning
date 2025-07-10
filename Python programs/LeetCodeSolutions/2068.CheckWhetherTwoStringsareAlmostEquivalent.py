"""
LeetCode 2068. Check Whether Two Strings are Almost Equivalent

Given two strings word1 and word2, return true if the difference in the number of occurrences of every letter is at most 3.

Example:
Input: word1 = "aaaa", word2 = "bccb"
Output: false

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist only of lowercase English letters.
"""

def checkAlmostEquivalent(word1, word2):
    from collections import Counter
    c1 = Counter(word1)
    c2 = Counter(word2)
    for ch in set(word1 + word2):
        if abs(c1[ch] - c2[ch]) > 3:
            return False
    return True

# Example usage:
# print(checkAlmostEquivalent("aaaa", "bccb"))  # Output: False
