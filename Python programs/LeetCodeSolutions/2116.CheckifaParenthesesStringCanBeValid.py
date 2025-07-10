"""
LeetCode 2116. Check if a Parentheses String Can Be Valid

Given a string s and locked, return true if the string can be made valid.

Example:
Input: s = ")()))", locked = "01000"
Output: true

Constraints:
- n == s.length == locked.length
- 1 <= n <= 10^5
- s[i] is '(' or ')'
- locked[i] is '0' or '1'
"""

def canBeValid(s, locked):
    if len(s) % 2:
        return False
    lo = hi = 0
    for i, c in enumerate(s):
        if locked[i] == '0' or c == '(': lo += 1
        else: lo -= 1
        if locked[i] == '0' or c == ')': hi -= 1
        else: hi += 1
        if hi < 0: return False
        lo = max(lo, 0)
    return lo == 0

# Example usage:
# print(canBeValid(")()))", "01000"))  # Output: True
