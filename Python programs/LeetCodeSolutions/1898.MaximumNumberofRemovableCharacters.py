"""
LeetCode 1898. Maximum Number of Removable Characters

Given strings s and p, and an integer array removable, return the maximum k such that p is a subsequence of s after removing the first k indices in removable.

Example:
Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2

Constraints:
- 1 <= p.length <= s.length <= 10^5
- s and p consist of lowercase English letters.
- 1 <= removable.length < s.length
- 0 <= removable[i] < s.length
"""

def maximumRemovals(s, p, removable):
    def is_subseq(k):
        removed = set(removable[:k])
        j = 0
        for i, c in enumerate(s):
            if i in removed: continue
            if j < len(p) and c == p[j]:
                j += 1
        return j == len(p)
    left, right = 0, len(removable)
    while left < right:
        mid = (left + right + 1) // 2
        if is_subseq(mid):
            left = mid
        else:
            right = mid - 1
    return left

# Example usage:
# print(maximumRemovals("abcacb", "ab", [3,1,0]))  # Output: 2
