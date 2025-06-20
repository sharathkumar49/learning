"""
467. Unique Substrings in Wraparound String

Given a string s, return the number of unique non-empty substrings of s that are present in the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz".

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

Example:
Input: s = "zab"
Output: 6
"""

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        k = 0
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                k += 1
            else:
                k = 1
            idx = ord(s[i]) - ord('a')
            dp[idx] = max(dp[idx], k)
        return sum(dp)

# Example usage:
sol = Solution()
print(sol.findSubstringInWraproundString("zab"))  # Output: 6
