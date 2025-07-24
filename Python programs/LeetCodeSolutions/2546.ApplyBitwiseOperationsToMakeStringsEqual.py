"""
LeetCode 2546. Apply Bitwise Operations to Make Strings Equal

Given two binary strings, return True if you can make them equal using allowed operations.

Constraints:
- 1 <= s.length == t.length <= 10^5
"""

def makeStringsEqual(s, t):
    return ("1" in s) == ("1" in t)
# Example usage:
# print(makeStringsEqual("1010","0110"))  # Output: True
