"""
LeetCode 1808. Maximize Number of Nice Divisors

Given a positive integer primeFactors, return the maximum number of nice divisors you can get.

Example 1:
Input: primeFactors = 5
Output: 6

Constraints:
- 1 <= primeFactors <= 10^9
"""

def maxNiceDivisors(primeFactors):
    MOD = 10**9+7
    if primeFactors <= 3:
        return primeFactors
    q, r = divmod(primeFactors, 3)
    if r == 0:
        return pow(3, q, MOD)
    if r == 1:
        return pow(3, q-1, MOD) * 4 % MOD
    return pow(3, q, MOD) * 2 % MOD

# Example usage:
# primeFactors = 5
# print(maxNiceDivisors(primeFactors))  # Output: 6
