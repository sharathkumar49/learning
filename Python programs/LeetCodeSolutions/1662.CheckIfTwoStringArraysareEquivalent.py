"""
LeetCode 1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string when concatenated.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true

Constraints:
- 1 <= word1.length, word2.length <= 10^3
- 1 <= word1[i].length, word2[i].length <= 10^3
- 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
- word1[i] and word2[i] consist of lowercase letters.
"""

def arrayStringsAreEqual(word1, word2):
    return ''.join(word1) == ''.join(word2)

# Example usage:
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# print(arrayStringsAreEqual(word1, word2))  # Output: True
