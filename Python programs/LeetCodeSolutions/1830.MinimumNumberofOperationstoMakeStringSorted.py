"""
LeetCode 1830. Minimum Number of Operations to Make String Sorted

Given a string s, return the minimum number of operations to make s sorted as described in the problem.

Example 1:
Input: s = "cba"
Output: 5

Constraints:
- 1 <= s.length <= 3000
- s consists of lowercase English letters
"""

def makeStringSorted(s):
    MOD = 10**9+7
    from math import factorial
    n = len(s)
    freq = [0]*26
    for c in s:
        freq[ord(c)-97] += 1
    res = 0
    for i in range(n):
        less = sum(freq[:ord(s[i])-97])
        if less:
            f = factorial(n-i-1)
            for v in freq:
                f //= factorial(v)
            res = (res + less * f) % MOD
        freq[ord(s[i])-97] -= 1
    return res

# Example usage:
# s = "cba"
# print(makeStringSorted(s))  # Output: 5
