"""
LeetCode 1446. Consecutive Characters

Given a string s, return the maximum number of consecutive identical characters in s.

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters.

Example:
Input: s = "leetcode"
Output: 2
"""
def maxPower(s):
    res = cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 1
    return res

# Example usage:
s = "leetcode"
print(maxPower(s))  # Output: 2
