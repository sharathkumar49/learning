"""
LeetCode 2413. Smallest Even Multiple

Given n, return the smallest even multiple of n.

Constraints:
- 1 <= n <= 150
"""

def smallestEvenMultiple(n):
    return n if n%2==0 else n*2

# Example usage:
# print(smallestEvenMultiple(5))  # Output: 10
