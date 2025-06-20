"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

Constraints:
- -2^31 <= n <= 2^31 - 1

Follow up: Could you do it without using any loops or recursion?
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

# Example usage:
n = 27
print(Solution().isPowerOfThree(n))  # Output: True
