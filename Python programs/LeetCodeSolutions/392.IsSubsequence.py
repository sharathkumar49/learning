"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)

# Example usage:
s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))  # Output: True
