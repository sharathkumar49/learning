"""
LeetCode 1768. Merge Strings Alternately

Given two strings word1 and word2, merge them by alternating characters.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters
"""

def mergeAlternately(word1, word2):
    res = []
    i = j = 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res.append(word1[i])
            i += 1
        if j < len(word2):
            res.append(word2[j])
            j += 1
    return ''.join(res)

# Example usage:
# word1 = "abc"
# word2 = "pqr"
# print(mergeAlternately(word1, word2))  # Output: "apbqcr"
