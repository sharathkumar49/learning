"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.

Example:
Input: s = "abab"
Output: True
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

# Example usage:
sol = Solution()
print(sol.repeatedSubstringPattern("abab"))  # Output: True
