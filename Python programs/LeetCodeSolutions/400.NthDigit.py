"""
400. Nth Digit

Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, ...].

Constraints:
- 1 <= n <= 2^31 - 1
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        start = 1
        count = 9
        while n > count:
            n -= count
            digit += 1
            start *= 10
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])

# Example usage:
n = 11
print(Solution().findNthDigit(n))  # Output: 0
