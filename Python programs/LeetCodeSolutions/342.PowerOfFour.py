"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

Constraints:
- -2^31 <= n <= 2^31 - 1
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

# Example usage:
n = 16
print(Solution().isPowerOfFour(n))  # Output: True
