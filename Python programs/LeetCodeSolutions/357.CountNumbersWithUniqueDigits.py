"""
357. Count Numbers with Unique Digits

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.

Constraints:
- 0 <= n <= 8
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res, unique = 10, 9
        for i in range(2, n+1):
            unique *= (11 - i)
            res += unique
        return res

# Example usage:
n = 2
print(Solution().countNumbersWithUniqueDigits(n))  # Output: 91
