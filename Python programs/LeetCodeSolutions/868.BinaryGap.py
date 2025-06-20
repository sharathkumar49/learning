"""
868. Binary Gap

Given a positive integer n, return the longest distance between two consecutive 1's in the binary representation of n.

Example 1:
Input: n = 22
Output: 2

Example 2:
Input: n = 8
Output: 0

Constraints:
- 1 <= n <= 10^9
"""
def binaryGap(n):
    last = res = 0
    i = 1
    while n:
        if n & 1:
            if last:
                res = max(res, i - last)
            last = i
        n >>= 1
        i += 1
    return res

# Example usage:
print(binaryGap(22))  # Output: 2
print(binaryGap(8))   # Output: 0
