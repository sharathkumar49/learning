"""
LeetCode 1647. Minimum Deletions to Make Character Frequencies Unique

Given a string s, return the minimum number of deletions needed so that no two characters have the same frequency.

Example 1:
Input: s = "aab"
Output: 0

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

def minDeletions(s):
    from collections import Counter
    freq = list(Counter(s).values())
    freq.sort(reverse=True)
    res = 0
    used = set()
    for f in freq:
        while f > 0 and f in used:
            f -= 1
            res += 1
        used.add(f)
    return res

# Example usage:
# s = "aab"
# print(minDeletions(s))  # Output: 0
