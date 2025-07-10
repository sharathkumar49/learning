"""
LeetCode 1651. Hexspeak

Given a positive integer num, return its representation in hexspeak. Replace 0 with 'O', 1 with 'I', and only allow 'A'-'F', 'I', 'O'. If not possible, return "ERROR".

Example 1:
Input: num = 257
Output: "IOI"

Constraints:
- 1 <= num <= 10^12
"""

def toHexspeak(num):
    s = hex(num)[2:].upper().replace('0','O').replace('1','I')
    for c in s:
        if c not in 'ABCDEFIO':
            return "ERROR"
    return s

# Example usage:
# num = 257
# print(toHexspeak(num))  # Output: "IOI"
