"""
LeetCode 2405. Optimal Partition of String

Given a string, partition it into as few substrings as possible so that no letter appears in more than one substring.

Constraints:
- 1 <= s.length <= 10^5
"""

def partitionString(s):
    seen = set()
    res = 1
    for c in s:
        if c in seen:
            res += 1
            seen = set()
        seen.add(c)
    return res

# Example usage:
# print(partitionString("abacaba"))  # Output: 4
