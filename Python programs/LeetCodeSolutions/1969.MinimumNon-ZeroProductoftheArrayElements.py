"""
LeetCode 1969. Minimum Non-Zero Product of the Array Elements

Given an integer p, return the minimum non-zero product of the array [1, 2, ..., 2^p - 1] modulo 10^9+7.

Example:
Input: p = 1
Output: 1

Constraints:
- 1 <= p <= 60
"""

MOD = 10**9+7

def minNonZeroProduct(p):
    n = (1 << p) - 1
    return pow(n-1, n//2, MOD) * (n % MOD) % MOD

# Example usage:
# print(minNonZeroProduct(1))  # Output: 1
