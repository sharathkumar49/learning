"""
LeetCode 1784. Check if Binary String Has at Most One Segment of Ones

Given a binary string s, return true if it contains at most one segment of ones.

Example 1:
Input: s = "1001"
Output: False

Constraints:
- 1 <= s.length <= 100
- s[i] is '0' or '1'
"""

def checkOnesSegment(s):
    return '01' not in s

# Example usage:
# s = "1001"
# print(checkOnesSegment(s))  # Output: False
