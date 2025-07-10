"""
LeetCode 2119. A Number After a Double Reversal

Given an integer num, return true if num is the same after a double reversal.

Example:
Input: num = 526
Output: true

Constraints:
- 0 <= num <= 10^6
"""

def isSameAfterReversals(num):
    return num == 0 or num % 10 != 0

# Example usage:
# print(isSameAfterReversals(526))  # Output: True
