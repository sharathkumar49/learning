"""
LeetCode 1614. Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the maximum nesting depth of the parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3

Constraints:
- 1 <= s.length <= 100
- s consists of digits, '+', '-', '*', '/', '(', ')', and ' '.
"""

def maxDepth(s):
    res = cur = 0
    for c in s:
        if c == '(': cur += 1
        res = max(res, cur)
        if c == ')': cur -= 1
    return res

# Example usage:
# s = "(1+(2*3)+((8)/4))+1"
# print(maxDepth(s))  # Output: 3
