"""
340. Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Constraints:
- 1 <= s.length <= 5 * 10^4
- 0 <= k <= 50
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
        left = 0
        count = {}
        res = 0
        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res

# Example usage:
s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))  # Output: 3
