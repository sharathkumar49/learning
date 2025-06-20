"""
479. Largest Palindrome Product

Given an integer n, return the largest palindrome made from the product of two n-digit numbers. Since the answer can be very large, return it modulo 1337.

Constraints:
- 1 <= n <= 8

Example:
Input: n = 2
Output: 987
"""

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10**n - 1
        lower = 10**(n-1)
        for left in range(upper, lower-1, -1):
            p = int(str(left) + str(left)[::-1])
            for x in range(upper, lower-1, -1):
                if p // x > upper:
                    break
                if p % x == 0:
                    return p % 1337
        return -1

# Example usage:
sol = Solution()
print(sol.largestPalindrome(2))  # Output: 987
