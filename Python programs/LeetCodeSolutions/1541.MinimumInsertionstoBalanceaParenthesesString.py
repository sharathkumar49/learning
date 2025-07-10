"""
LeetCode 1541. Minimum Insertions to Balance a Parentheses String

Given a parentheses string s, return the minimum number of insertions needed to make the string valid. A string is valid if every '(' has two consecutive ')' after it.

Constraints:
- 1 <= s.length <= 10^5
- s consists of '(' and ')'

Example:
Input: s = "(()))"
Output: 1
"""
def minInsertions(s):
    res = 0
    need = 0
    for c in s:
        if c == '(': 
            need += 2
            if need % 2:
                res += 1
                need -= 1
        else:
            need -= 1
            if need < 0:
                res += 1
                need = 1
    return res + need

# Example usage:
s = "(()))"
print(minInsertions(s))  # Output: 1
