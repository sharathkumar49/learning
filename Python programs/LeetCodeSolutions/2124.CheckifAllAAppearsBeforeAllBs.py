"""
LeetCode 2124. Check if All A's Appears Before All B's

Given a string s, return true if all 'a's appear before all 'b's.

Example:
Input: s = "aaabbb"
Output: true

Constraints:
- 1 <= s.length <= 100
- s consists only of 'a' and 'b'.
"""

def checkString(s):
    return 'ba' not in s

# Example usage:
# print(checkString("aaabbb"))  # Output: True
