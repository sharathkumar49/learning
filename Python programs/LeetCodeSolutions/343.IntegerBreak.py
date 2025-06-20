"""
343. Integer Break

Given an integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Constraints:
- 2 <= n <= 58
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

# Example usage:
n = 10
print(Solution().integerBreak(n))  # Output: 36
