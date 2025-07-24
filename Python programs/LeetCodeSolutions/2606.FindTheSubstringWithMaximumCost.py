"""
LeetCode 2606. Find the Substring With Maximum Cost

Given s, chars, and vals, return the maximum cost substring.

Constraints:
- 1 <= s.length <= 10^5
"""

def maximumCostSubstring(s, chars, vals):
    d = {c: v for c, v in zip(chars, vals)}
    arr = [d.get(c, ord(c)-ord('a')+1) for c in s]
    res = cur = 0
    for x in arr:
        cur = max(x, cur + x)
        res = max(res, cur)
    return res
# Example usage:
# print(maximumCostSubstring("adaa", "d", [-1000]))  # Output: 2
