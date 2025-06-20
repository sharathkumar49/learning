"""
LeetCode 693. Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111

Constraints:
- 1 <= n <= 2^31 - 1
"""
def hasAlternatingBits(n: int) -> bool:
    prev = n & 1
    n >>= 1
    while n:
        curr = n & 1
        if curr == prev:
            return False
        prev = curr
        n >>= 1
    return True

# Example usage
if __name__ == "__main__":
    print(hasAlternatingBits(5))  # Output: True
    print(hasAlternatingBits(7))  # Output: False
