"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
Given n, calculate F(n).

Constraints:
- 0 <= n <= 30

Example:
Input: n = 2
Output: 1
"""

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Example usage:
sol = Solution()
print(sol.fib(2))  # Output: 1
