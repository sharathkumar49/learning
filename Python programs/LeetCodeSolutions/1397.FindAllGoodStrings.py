"""
LeetCode 1397. Find All Good Strings

Given the strings s1, s2, evil, and an integer n, return the number of good strings of length n lexicographically between s1 and s2 (inclusive) that do not contain the string evil as a substring. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 500
- s1.length == s2.length == n
- 1 <= evil.length <= n
- All strings consist of lowercase English letters.

Example:
Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51
"""
def findGoodStrings(n, s1, s2, evil):
    MOD = 10**9+7
    from functools import lru_cache
    def build_kmp(evil):
        m = len(evil)
        fail = [0]*m
        for i in range(1, m):
            j = fail[i-1]
            while j and evil[i] != evil[j]:
                j = fail[j-1]
            if evil[i] == evil[j]:
                j += 1
            fail[i] = j
        return fail
    fail = build_kmp(evil)
    @lru_cache(None)
    def dp(pos, tight1, tight2, evil_idx):
        if evil_idx == len(evil): return 0
        if pos == n: return 1
        res = 0
        lo = s1[pos] if tight1 else 'a'
        hi = s2[pos] if tight2 else 'z'
        for c in map(chr, range(ord(lo), ord(hi)+1)):
            j = evil_idx
            while j and c != evil[j]:
                j = fail[j-1]
            if c == evil[j]:
                j += 1
            res = (res + dp(pos+1, tight1 and c==lo, tight2 and c==hi, j)) % MOD
        return res
    return dp(0, True, True, 0)

# Example usage:
n = 2
s1 = "aa"
s2 = "da"
evil = "b"
print(findGoodStrings(n, s1, s2, evil))  # Output: 51
