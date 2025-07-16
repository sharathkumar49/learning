"""
LeetCode 2351. First Letter to Appear Twice

Given s, return the first letter to appear twice.

Example:
Input: s = "abccbaacz"
Output: "c"

Constraints:
- 2 <= s.length <= 100
- s consists of lowercase English letters
"""

def repeatedCharacter(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)

# Example usage:
# print(repeatedCharacter("abccbaacz"))  # Output: "c"
