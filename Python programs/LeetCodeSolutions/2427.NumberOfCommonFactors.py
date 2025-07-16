"""
LeetCode 2427. Number of Common Factors

Given two integers, return the number of common factors.

Constraints:
- 1 <= a, b <= 1000
"""

def commonFactors(a, b):
    return sum(a%i==0 and b%i==0 for i in range(1, min(a,b)+1))

# Example usage:
# print(commonFactors(12,6))  # Output: 4
