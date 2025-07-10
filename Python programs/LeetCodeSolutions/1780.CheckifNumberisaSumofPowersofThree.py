"""
LeetCode 1780. Check if Number is a Sum of Powers of Three

Given an integer n, return true if it can be represented as a sum of distinct powers of three.

Example 1:
Input: n = 12
Output: true

Constraints:
- 1 <= n <= 10^7
"""

def checkPowersOfThree(n):
    while n:
        if n % 3 == 2:
            return False
        n //= 3
    return True

# Example usage:
# n = 12
# print(checkPowersOfThree(n))  # Output: True
