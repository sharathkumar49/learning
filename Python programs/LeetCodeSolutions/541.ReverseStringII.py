"""
541. Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only lowercase English letters.
- 1 <= k <= 10^4

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)

# Example usage:
sol = Solution()
print(sol.reverseStr("abcdefg", 2))  # Output: "bacdfeg"
