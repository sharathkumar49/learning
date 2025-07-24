"""
LeetCode 2652. Sum Multiples

Given n, return the sum of all numbers in the range [1, n] that are multiples of 3, 5, or 7.

Constraints:
- 1 <= n <= 10^3
"""

def sumOfMultiples(n):
    return sum(x for x in range(1, n+1) if x%3==0 or x%5==0 or x%7==0)
# Example usage:
# print(sumOfMultiples(7))  # Output: 21
