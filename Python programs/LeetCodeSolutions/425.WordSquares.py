"""
425. Word Squares

Given a set of words (without duplicates), find all word squares you can build from them.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 5
- All words have the same length.
- All words consist of only lowercase English letters.
"""
from typing import List
from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        prefix_map = defaultdict(list)
        for word in words:
            for i in range(n):
                prefix_map[word[:i]].append(word)
        res = []
        def backtrack(square):
            if len(square) == n:
                res.append(square[:])
                return
            prefix = ''.join([w[len(square)] for w in square])
            for candidate in prefix_map[prefix]:
                backtrack(square + [candidate])
        for word in words:
            backtrack([word])
        return res

# Example usage:
words = ["area","lead","wall","lady","ball"]
print(Solution().wordSquares(words))
# Output: [["wall","area","lead","lady"],["ball","area","lead","lady"]]
