"""
LeetCode 2268. Minimum Number of Keypresses

Given s, return the minimum number of keypresses needed to type s.

Example:
Input: s = "aabbcc"
Output: 6

Constraints:
- 1 <= s.length <= 100
"""

def minimumKeypresses(s):
    from collections import Counter
    freq = Counter(s)
    freq = sorted(freq.values(), reverse=True)
    res = 0
    for i, f in enumerate(freq):
        res += f * (1 + (i//9))
    return res

# Example usage:
# print(minimumKeypresses("aabbcc"))  # Output: 6
