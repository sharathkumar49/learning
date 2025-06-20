"""
263. Ugly Number
https://leetcode.com/problems/ugly-number/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Constraints:
- -2^31 <= n <= 2^31 - 1

Example 1:
Input: n = 6
Output: true

Example 2:
Input: n = 1
Output: true

Example 3:
Input: n = 14
Output: false
"""
def isUgly(n):
    if n <= 0:
        return False
    for f in [2, 3, 5]:
        while n % f == 0:
            n //= f
    return n == 1

# Example usage:
if __name__ == "__main__":
    print(isUgly(6))   # Output: True
    print(isUgly(1))   # Output: True
    print(isUgly(14))  # Output: False
