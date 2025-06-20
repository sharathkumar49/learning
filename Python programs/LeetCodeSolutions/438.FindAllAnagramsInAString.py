"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.

Example:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        res = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            s_count[s[i]] += 1
            if s_count == p_count:
                res.append(i-len(p)+1)
            s_count[s[i-len(p)+1]] -= 1
            if s_count[s[i-len(p)+1]] == 0:
                del s_count[s[i-len(p)+1]]
        return res

# Example usage:
sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
