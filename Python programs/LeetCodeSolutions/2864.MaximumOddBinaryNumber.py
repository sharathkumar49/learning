"""
LeetCode 2864. Maximum Odd Binary Number

Given s, return the maximum odd binary number.

Constraints:
- 1 <= s.length <= 100
"""

def maximumOddBinaryNumber(s):
    ones = s.count('1')
    zeros = len(s) - ones
    return '1' * (ones - 1) + '0' * zeros + '1'
# Example usage:
# print(maximumOddBinaryNumber("010"))  # Output: "100"
