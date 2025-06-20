"""
472. Concatenated Words

Given an array of strings words, return all the concatenated words in the given list of words. A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Constraints:
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 30
- words[i] consists of only lowercase English letters.
- All the strings in words are unique.

Example:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list) -> list:
        word_set = set(words)
        res = []
        def canForm(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and (suffix in word_set or canForm(suffix)):
                    return True
            return False
        for word in words:
            word_set.remove(word)
            if canForm(word):
                res.append(word)
            word_set.add(word)
        return res

# Example usage:
sol = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(sol.findAllConcatenatedWordsInADict(words))  # Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
