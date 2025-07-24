"""
LeetCode 2645. Minimum Additions to Make Valid String

Given s, return the minimum number of additions to make it valid.

Constraints:
- 1 <= s.length <= 100
"""

def addMinimum(s):
    res = 0
    i = 0
    while i < len(s):
        if s[i:i+3] == 'abc':
            i += 3
        else:
            need = 3 - len(set(s[i:i+3]))
            res += need
            i += 1
    return res
# Example usage:
# print(addMinimum("b"))  # Output: 2
