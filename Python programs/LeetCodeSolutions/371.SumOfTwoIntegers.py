"""
371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Constraints:
- -2^31 <= a, b <= 2^31 - 1
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)

# Example usage:
a = 1
b = 2
print(Solution().getSum(a, b))  # Output: 3
