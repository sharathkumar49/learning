"""
422. Valid Word Square

Given a sequence of words, check whether it forms a valid word square.

Constraints:
- 1 <= words.length <= 500
- 1 <= words[i].length <= 500
- words[i] consists of only lowercase English letters.
"""
from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True

# Example usage:
words = ["abcd","bnrt","crmy","dtye"]
print(Solution().validWordSquare(words))  # Output: True
