"""
910. Smallest Subsequence of Distinct Characters
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Example:
Input: s = "bcabc"
Output: "abc"
"""
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return ''.join(stack)

# Example usage
if __name__ == "__main__":
    s = "bcabc"
    print(Solution().smallestSubsequence(s))  # Output: "abc"
