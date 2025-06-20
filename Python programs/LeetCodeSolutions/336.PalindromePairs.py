"""
336. Palindrome Pairs

Given a list of unique words, return all the pairs of distinct indices (i, j) in the given list, so that the concatenation of words[i] + words[j] is a palindrome.

Constraints:
- 1 <= words.length <= 5000
- 0 <= words[i].length <= 300
- words[i] consists of lowercase English letters.
"""
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        word_dict = {w: i for i, w in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]
                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in word_dict:
                        res.append([word_dict[back], i])
                if j != len(word) and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in word_dict:
                        res.append([i, word_dict[back]])
        return res

# Example usage:
words = ["abcd","dcba","lls","s","sssll"]
print(Solution().palindromePairs(words))  # Output: [[1,0],[0,1],[3,2],[2,4]]
