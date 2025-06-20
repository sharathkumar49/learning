"""
500. Keyboard Row

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of the American keyboard.

Constraints:
- 1 <= words.length <= 20
- 1 <= words[i].length <= 100
- words[i] consists of English letters (both lowercase and uppercase).

Example:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
"""

class Solution:
    def findWords(self, words: list) -> list:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for word in words:
            wset = set(word.lower())
            if any(wset <= row for row in rows):
                res.append(word)
        return res

# Example usage:
sol = Solution()
print(sol.findWords(["Hello","Alaska","Dad","Peace"]))  # Output: ["Alaska","Dad"]
