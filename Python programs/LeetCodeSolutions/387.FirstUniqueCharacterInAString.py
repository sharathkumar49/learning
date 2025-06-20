"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

# Example usage:
s = "leetcode"
print(Solution().firstUniqChar(s))  # Output: 0
