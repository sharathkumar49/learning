"""
LeetCode 2710. Remove Trailing Zeros From a String

Given num, return the string after removing trailing zeros.

Constraints:
- 1 <= num.length <= 100
"""

def removeTrailingZeros(num):
    return num.rstrip('0')
# Example usage:
# print(removeTrailingZeros("51230100"))  # Output: "512301"
