"""
LeetCode 2544. Alternating Digit Sum

Given an integer n, return the alternating digit sum.

Constraints:
- 1 <= n <= 10^9
"""

def alternateDigitSum(n):
    s = str(n)
    return sum(int(d) if i%2==0 else -int(d) for i,d in enumerate(s))
# Example usage:
# print(alternateDigitSum(521))  # Output: 4
