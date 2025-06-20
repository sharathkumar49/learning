"""
1081. Smallest Subsequence of Distinct Characters

Return the lexicographically smallest subsequence of the given string that contains all the distinct characters of the string exactly once.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Example:
Input: s = "bcabc"
Output: "abc"
"""
def smallestSubsequence(s: str) -> str:
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
print(smallestSubsequence(s))  # Output: "abc"
