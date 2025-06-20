"""
LeetCode 678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The '*' can be treated as '(', ')' or an empty string.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.
"""
def checkValidString(s: str) -> bool:
    low = high = 0
    for c in s:
        if c == '(': low += 1; high += 1
        elif c == ')': low -= 1; high -= 1
        else: low -= 1; high += 1
        if high < 0: return False
        if low < 0: low = 0
    return low == 0

# Example usage
if __name__ == "__main__":
    print(checkValidString("()"))    # Output: True
    print(checkValidString("(*)"))   # Output: True
    print(checkValidString("(*))"))  # Output: True
