"""
418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the sentence can be fitted on the screen.

Constraints:
- 1 <= rows, cols <= 20,000
- 1 <= sentence.length <= 100
- 1 <= sentence[i].length <= 10
- sentence[i] consists of non-empty words and contains only lowercase English letters.
"""
from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start = 0
        l = len(s)
        for _ in range(rows):
            start += cols
            if s[start % l] == ' ':
                start += 1
            else:
                while start > 0 and s[(start-1) % l] != ' ':
                    start -= 1
        return start // l

# Example usage:
sentence = ["hello", "world"]
rows = 2
cols = 8
print(Solution().wordsTyping(sentence, rows, cols))  # Output: 1
