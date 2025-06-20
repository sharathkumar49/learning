"""
87. Scramble String
https://leetcode.com/problems/scramble-string/

Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1.

Constraints:
- s1.length == s2.length
- 1 <= s1.length <= 30
- s1 and s2 consist of lowercase English letters.

Example:
Input: s1 = "great", s2 = "rgeat"
Output: true
"""
def isScramble(s1: str, s2: str) -> bool:
    from functools import lru_cache
    @lru_cache(None)
    def dfs(a, b):
        if a == b:
            return True
        if sorted(a) != sorted(b):
            return False
        n = len(a)
        for i in range(1, n):
            if (dfs(a[:i], b[:i]) and dfs(a[i:], b[i:])) or (dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i])):
                return True
        return False
    return dfs(s1, s2)

# Example usage:
if __name__ == "__main__":
    print(isScramble("great", "rgeat"))  # Output: True
    print(isScramble("abcde", "caebd")) # Output: False
