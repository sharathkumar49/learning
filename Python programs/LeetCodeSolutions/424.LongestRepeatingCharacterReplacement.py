"""
424. Longest Repeating Character Replacement

Given a string s and an integer k, return the length of the longest substring containing the same letter you can get after performing at most k replacements.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        left = 0
        max_count = 0
        count = Counter()
        res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            while right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# Example usage:
s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))  # Output: 4
