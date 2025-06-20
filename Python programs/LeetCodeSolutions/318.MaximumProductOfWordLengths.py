"""
318. Maximum Product of Word Lengths

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Constraints:
- 2 <= words.length <= 1000
- 1 <= words[i].length <= 1000
- words[i] consists only of lowercase English letters.
"""
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        for i, word in enumerate(words):
            for c in word:
                masks[i] |= 1 << (ord(c) - ord('a'))
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

# Example usage:
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(Solution().maxProduct(words))  # Output: 16
