"""
482. License Key Formatting

Given a string s and an integer k, format the string such that every group contains exactly k characters, except for the first group which could be shorter. All lowercase letters should be converted to uppercase.

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters, digits, and '-'.
- 1 <= k <= 10^4

Example:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        size = len(s)
        first = size % k or k
        res = s[:first]
        for i in range(first, size, k):
            res += '-' + s[i:i+k]
        return res

# Example usage:
sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # Output: "5F3Z-2E9W"
