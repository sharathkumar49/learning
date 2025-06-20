"""
408. Valid Word Abbreviation

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

Constraints:
- 1 <= word.length <= 20
- 1 <= abbr.length <= 20
- word consists of only lowercase English letters.
- abbr consists of lowercase English letters and digits.
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)

# Example usage:
word = "internationalization"
abbr = "i12iz4n"
print(Solution().validWordAbbreviation(word, abbr))  # Output: True
