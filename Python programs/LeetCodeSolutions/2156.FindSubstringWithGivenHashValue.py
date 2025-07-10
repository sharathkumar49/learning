"""
LeetCode 2156. Find Substring With Given Hash Value

Given a string s, an integer power, modulo, k, and hashValue, return the substring of length k whose hash equals hashValue as defined by the rolling hash function. The answer is guaranteed to be unique.

Example:
Input: s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
Output: "ee"

Constraints:
- 1 <= k <= s.length <= 3 * 10^5
- 1 <= power, modulo <= 10^9
- 0 <= hashValue < modulo
- s consists of lowercase English letters.
"""

def subStrHash(s, power, modulo, k, hashValue):
    n = len(s)
    res = 0
    pk = pow(power, k, modulo)
    h = 0
    ans = ''
    for i in range(n-1, -1, -1):
        h = (h * power + ord(s[i]) - ord('a') + 1) % modulo
        if i + k < n:
            h = (h - (ord(s[i+k]) - ord('a') + 1) * pk) % modulo
        if i + k <= n and h == hashValue:
            ans = s[i:i+k]
    return ans

# Example usage:
# print(subStrHash("leetcode", 7, 20, 2, 0))  # Output: "ee"
