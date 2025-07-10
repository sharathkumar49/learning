"""
LeetCode 1754. Largest Merge Of Two Strings

Given two strings word1 and word2, return the lexicographically largest merge of the two strings.

Example 1:
Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"

Constraints:
- 1 <= word1.length, word2.length <= 3000
- word1 and word2 consist only of lowercase English letters
"""

def largestMerge(word1, word2):
    res = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        if word1[i:] > word2[j:]:
            res.append(word1[i])
            i += 1
        else:
            res.append(word2[j])
            j += 1
    res.extend(word1[i:])
    res.extend(word2[j:])
    return ''.join(res)

# Example usage:
# word1 = "cabaa"
# word2 = "bcaaa"
# print(largestMerge(word1, word2))  # Output: "cbcabaaaaa"
