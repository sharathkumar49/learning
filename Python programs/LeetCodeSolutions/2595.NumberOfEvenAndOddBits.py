"""
LeetCode 2595. Number of Even and Odd Bits

Given an integer n, return the number of even and odd bits in its binary representation.

Constraints:
- 1 <= n <= 10^9
"""

def evenOddBit(n):
    even = odd = 0
    i = 0
    while n:
        if n & 1:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        n >>= 1
        i += 1
    return [even, odd]
# Example usage:
# print(evenOddBit(17))  # Output: [2,0]
