"""
LeetCode 1680. Concatenation of Consecutive Binary Numbers

Given an integer n, return the decimal value of the concatenation of the binary representations of 1 to n, modulo 10^9+7.

Example 1:
Input: n = 3
Output: 27

Constraints:
- 1 <= n <= 10^5
"""

def concatenatedBinary(n):
    mod = 10**9+7
    res = 0
    for i in range(1, n+1):
        l = i.bit_length()
        res = ((res << l) | i) % mod
    return res

# Example usage:
# n = 3
# print(concatenatedBinary(n))  # Output: 27
