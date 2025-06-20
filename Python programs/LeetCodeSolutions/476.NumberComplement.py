"""
476. Number Complement

Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

Constraints:
- 1 <= num < 2^31

Example:
Input: num = 5
Output: 2
"""

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask <<= 1
        return (mask - 1) ^ num

# Example usage:
sol = Solution()
print(sol.findComplement(5))  # Output: 2
