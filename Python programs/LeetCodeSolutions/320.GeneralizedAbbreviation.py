"""
320. Generalized Abbreviation

A word's generalized abbreviation can be constructed by replacing any number of non-overlapping substrings with their respective lengths. Given a word, return a list of all generalized abbreviations of the word.

Constraints:
- 1 <= word.length <= 15
- word consists of only lowercase English letters.
"""
from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        def backtrack(pos, cur, count):
            if pos == len(word):
                res.append(cur + (str(count) if count > 0 else ''))
                return
            backtrack(pos + 1, cur, count + 1)
            backtrack(pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0)
        backtrack(0, '', 0)
        return res

# Example usage:
word = "word"
print(Solution().generateAbbreviations(word))
# Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
