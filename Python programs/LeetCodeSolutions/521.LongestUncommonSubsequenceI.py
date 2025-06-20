"""
521. Longest Uncommon Subsequence I

Given two strings a and b, return the length of the longest uncommon subsequence between them. If no such subsequence exists, return -1.

Constraints:
- 1 <= a.length, b.length <= 100
- a and b consist of lower-case English letters.

Example:
Input: a = "aba", b = "cdc"
Output: 3
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1

# Example usage:
sol = Solution()
print(sol.findLUSlength("aba", "cdc"))  # Output: 3
