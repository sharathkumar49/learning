"""
878. Nth Magical Number

A positive integer is magical if it is divisible by either a or b. Return the n-th magical number. Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1, a = 2, b = 3
Output: 2

Example 2:
Input: n = 4, a = 2, b = 3
Output: 6

Constraints:
- 1 <= n <= 10^9
- 2 <= a, b <= 4 * 10^4
"""
def nthMagicalNumber(n, a, b):
    from math import gcd
    MOD = 10**9 + 7
    lcm = a * b // gcd(a, b)
    l, r = 1, n * min(a, b)
    while l < r:
        m = (l + r) // 2
        if m // a + m // b - m // lcm < n:
            l = m + 1
        else:
            r = m
    return l % MOD

# Example usage:
print(nthMagicalNumber(1, 2, 3))  # Output: 2
print(nthMagicalNumber(4, 2, 3))  # Output: 6
