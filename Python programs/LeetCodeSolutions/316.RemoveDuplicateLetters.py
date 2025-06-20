"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return ''.join(stack)

# Example usage:
s = "bcabc"
print(Solution().removeDuplicateLetters(s))  # Output: "abc"
