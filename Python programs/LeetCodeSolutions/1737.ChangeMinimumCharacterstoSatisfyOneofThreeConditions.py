"""
LeetCode 1737. Change Minimum Characters to Satisfy One of Three Conditions

Given two strings a and b, return the minimum number of characters to change to satisfy one of three conditions described in the problem.

Example 1:
Input: a = "aba", b = "caa"
Output: 2

Constraints:
- 1 <= a.length, b.length <= 10^5
- a and b consist of lowercase English letters
"""

def minCharacters(a, b):
    from collections import Counter
    ca = Counter(a)
    cb = Counter(b)
    res = float('inf')
    for c in range(ord('a'), ord('z')):
        c = chr(c)
        res = min(res, len(a) - sum(v for k, v in ca.items() if k < c) + len(b) - sum(v for k, v in cb.items() if k >= c))
        res = min(res, len(b) - sum(v for k, v in cb.items() if k < c) + len(a) - sum(v for k, v in ca.items() if k >= c))
    total = ca + cb
    res = min(res, len(a) + len(b) - max(total.values()))
    return res

# Example usage:
# a = "aba"
# b = "caa"
# print(minCharacters(a, b))  # Output: 2
