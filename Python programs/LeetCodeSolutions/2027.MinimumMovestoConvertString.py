"""
LeetCode 2027. Minimum Moves to Convert String

Given a string s, return the minimum number of moves to convert all 'X' to 'O'. Each move can convert up to three consecutive 'X' to 'O'.

Example:
Input: s = "XXOX"
Output: 2

Constraints:
- 1 <= s.length <= 1000
- s consists of 'X' and 'O'.
"""

def minimumMoves(s):
    i = 0
    res = 0
    while i < len(s):
        if s[i] == 'X':
            res += 1
            i += 3
        else:
            i += 1
    return res

# Example usage:
# print(minimumMoves("XXOX"))  # Output: 2
