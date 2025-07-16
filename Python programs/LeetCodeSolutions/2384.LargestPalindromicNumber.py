"""
LeetCode 2384. Largest Palindromic Number

Given a string num, return the largest palindromic number that can be constructed.

Constraints:
- 1 <= num.length <= 10^5
"""

def largestPalindromic(num):
    from collections import Counter
    count = Counter(num)
    left = []
    mid = ''
    for d in sorted(count.keys(), reverse=True):
        pairs = count[d] // 2
        left.extend([d]*pairs)
        count[d] -= pairs*2
    for d in sorted(count.keys(), reverse=True):
        if count[d]:
            mid = d
            break
    if left:
        res = ''.join(left) + mid + ''.join(reversed(left))
        return res.lstrip('0') or '0'
    return mid or '0'

# Example usage:
# print(largestPalindromic("444947137"))  # Output: "7449447"
