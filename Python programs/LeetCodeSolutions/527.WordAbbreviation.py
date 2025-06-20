"""
527. Word Abbreviation

Given an array of n non-empty strings, return a list of their minimal unique abbreviations.

Constraints:
- 1 <= words.length <= 400
- 1 <= words[i].length <= 20
- All words have only lowercase English letters.

Example:
Input: words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
Output: ["l2e","god","internal","me","i6l","interval","inte4n","f2e","intr4n"]
"""

def get_abbr(word, k):
    if len(word) - k <= 2:
        return word
    return word[:k] + str(len(word) - k - 1) + word[-1]

class Solution:
    def wordsAbbreviation(self, words: list) -> list:
        n = len(words)
        prefix = [1] * n
        abbr = [get_abbr(words[i], 1) for i in range(n)]
        while True:
            groups = {}
            for i, a in enumerate(abbr):
                groups.setdefault(a, []).append(i)
            unique = True
            for group in groups.values():
                if len(group) > 1:
                    unique = False
                    for i in group:
                        prefix[i] += 1
                        abbr[i] = get_abbr(words[i], prefix[i])
            if unique:
                break
        return abbr

# Example usage:
sol = Solution()
words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
print(sol.wordsAbbreviation(words))
# Output: ["l2e","god","internal","me","i6l","interval","inte4n","f2e","intr4n"]
