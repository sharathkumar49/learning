"""
LeetCode 1370. Increasing Decreasing String

Given a string s, return the string after sorting it in increasing then decreasing order repeatedly until all characters are used.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters only.

Example:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
"""
def sortString(s):
    from collections import Counter
    c = Counter(s)
    res = []
    while len(res) < len(s):
        for ch in sorted(c):
            if c[ch]:
                res.append(ch)
                c[ch] -= 1
        for ch in sorted(c, reverse=True):
            if c[ch]:
                res.append(ch)
                c[ch] -= 1
    return ''.join(res)

# Example usage:
s = "aaaabbbbcccc"
print(sortString(s))  # Output: "abccbaabccba"
