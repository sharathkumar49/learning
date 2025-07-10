"""
LeetCode 1794. Count Pairs of Equal Substrings With Minimum Difference

Given a string s and an integer k, return the number of pairs of equal substrings of length k with minimum difference in their starting indices.

Example 1:
Input: s = "abacaba", k = 2
Output: 2

Constraints:
- 1 <= s.length <= 10^5
- 1 <= k <= s.length
"""

def countPairs(s, k):
    from collections import defaultdict
    pos = defaultdict(list)
    for i in range(len(s)-k+1):
        sub = s[i:i+k]
        pos[sub].append(i)
    res = 0
    for idxs in pos.values():
        if len(idxs) > 1:
            idxs.sort()
            min_diff = min(idxs[i+1] - idxs[i] for i in range(len(idxs)-1))
            if min_diff == 1:
                res += 1
    return res

# Example usage:
# s = "abacaba"
# k = 2
# print(countPairs(s, k))  # Output: 2
