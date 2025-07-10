"""
LeetCode 1611. Minimum One Bit Operations to Make Integers Zero

Given an integer n, return the minimum number of operations to make n = 0. In one operation, you can flip the ith bit (0-indexed) if the (i-1)th bit is set to 1 and all lower bits are 0.

Example 1:
Input: n = 3
Output: 2

Constraints:
- 0 <= n <= 10^6
"""

def minimumOneBitOperations(n):
    if n == 0:
        return 0
    k = 0
    while (1 << (k + 1)) <= n:
        k += 1
    return (1 << (k + 1)) - 1 - minimumOneBitOperations(n ^ (1 << k))

# Example usage:
# n = 3
# print(minimumOneBitOperations(n))  # Output: 2
