"""
461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Constraints:
- 0 <= x, y <= 2^31 - 1

Example:
Input: x = 1, y = 4
Output: 2
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

# Example usage:
sol = Solution()
print(sol.hammingDistance(1, 4))  # Output: 2
