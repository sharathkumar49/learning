"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        res = 0
        odd = False
        for v in count.values():
            res += v // 2 * 2
            if v % 2:
                odd = True
        return res + odd

# Example usage:
s = "abccccdd"
print(Solution().longestPalindrome(s))  # Output: 7
