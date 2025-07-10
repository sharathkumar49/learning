"""
LeetCode 1837. Sum of Digits in Base K

Given an integer n and a base k, return the sum of digits of n in base k.

Example 1:
Input: n = 34, k = 6
Output: 9

Constraints:
- 1 <= n <= 100
- 2 <= k <= 10
"""

def sumBase(n, k):
    res = 0
    while n:
        res += n % k
        n //= k
    return res

# Example usage:
# n = 34
# k = 6
# print(sumBase(n, k))  # Output: 9
