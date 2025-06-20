"""
397. Integer Replacement

Given a positive integer n, return the minimum number of operations needed to reduce it to 1. You can perform either:
- If n is even, replace n with n / 2.
- If n is odd, replace n with either n + 1 or n - 1.

Constraints:
- 1 <= n <= 2^31 - 1
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or ((n >> 1) & 1) == 0:
                    n -= 1
                else:
                    n += 1
            count += 1
        return count

# Example usage:
n = 8
print(Solution().integerReplacement(n))  # Output: 3
