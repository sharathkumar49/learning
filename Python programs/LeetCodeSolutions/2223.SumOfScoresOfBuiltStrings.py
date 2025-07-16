"""
LeetCode 2223. Sum of Scores of Built Strings

Given a string s, return the sum of scores of all built strings.

Example:
Input: s = "babab"
Output: 9

Constraints:
- 1 <= s.length <= 10^6
- s consists of lowercase English letters
"""

def sumScores(s):
    n = len(s)
    z = [0]*n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l, r = i, i+z[i]-1
    return sum(z) + n

# Example usage:
# print(sumScores("babab"))  # Output: 9
