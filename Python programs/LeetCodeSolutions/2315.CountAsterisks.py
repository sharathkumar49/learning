"""
LeetCode 2315. Count Asterisks

Given s, return the number of asterisks not between pairs of vertical bars.

Example:
Input: s = "l|*e*et|c**o|*de|"
Output: 2

Constraints:
- 1 <= s.length <= 1000
"""

def countAsterisks(s):
    res = 0
    between = False
    for c in s:
        if c == '|':
            between = not between
        elif c == '*' and not between:
            res += 1
    return res

# Example usage:
# print(countAsterisks("l|*e*et|c**o|*de|"))  # Output: 2
