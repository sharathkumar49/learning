"""
LeetCode 1922. Count Good Numbers

Given an integer n, return the number of good digit strings of length n modulo 10^9+7. A good digit string has even indices with even digits and odd indices with prime digits.

Example:
Input: n = 1
Output: 5

Constraints:
- 1 <= n <= 10^15
"""

MOD = 10**9+7

def countGoodNumbers(n):
    def powmod(a, b):
        res = 1
        while b:
            if b % 2:
                res = res * a % MOD
            a = a * a % MOD
            b //= 2
        return res
    return powmod(5, (n+1)//2) * powmod(4, n//2) % MOD

# Example usage:
# print(countGoodNumbers(1))  # Output: 5
