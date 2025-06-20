"""
231. Power of Two
https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Constraints:
- -2^31 <= n <= 2^31 - 1

Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 16
Output: true

Example 3:
Input: n = 3
Output: false
"""
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Example usage:
if __name__ == "__main__":
    print(isPowerOfTwo(1))   # Output: True
    print(isPowerOfTwo(16))  # Output: True
    print(isPowerOfTwo(3))   # Output: False
