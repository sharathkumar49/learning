"""
520. Detect Capital

Given a word, return true if the usage of capitals in it is right.

Constraints:
- 1 <= word.length <= 100
- word consists of lowercase and uppercase English letters.

Example:
Input: word = "USA"
Output: true
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

# Example usage:
sol = Solution()
print(sol.detectCapitalUse("USA"))  # Output: True
