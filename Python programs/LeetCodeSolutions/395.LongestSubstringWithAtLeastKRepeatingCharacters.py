"""
395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only lowercase English letters.
- 1 <= k <= 10^5
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        from collections import Counter
        count = Counter(s)
        for c in count:
            if count[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

# Example usage:
s = "aaabb"
k = 3
print(Solution().longestSubstring(s, k))  # Output: 3
