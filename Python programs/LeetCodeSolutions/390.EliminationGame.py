"""
390. Elimination Game

You have a list arranged in a row: 1, 2, 3, ..., n. Every round, you eliminate the first number of the list, and every other number afterward, until one number remains. Return the last remaining number.

Constraints:
- 1 <= n <= 10^9
"""
class Solution:
    def lastRemaining(self, n: int) -> int:
        head, step, left = 1, 1, True
        while n > 1:
            if left or n % 2 == 1:
                head += step
            n //= 2
            step *= 2
            left = not left
        return head

# Example usage:
n = 9
print(Solution().lastRemaining(n))  # Output: 6
