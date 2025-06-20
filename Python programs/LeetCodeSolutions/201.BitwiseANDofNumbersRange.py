"""
201. Bitwise AND of Numbers Range
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Constraints:
- 0 <= left <= right <= 2^31 - 1

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0
"""
def rangeBitwiseAnd(left, right):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift

# Example usage:
if __name__ == "__main__":
    print(rangeBitwiseAnd(5, 7))           # Output: 4
    print(rangeBitwiseAnd(0, 0))           # Output: 0
    print(rangeBitwiseAnd(1, 2147483647))  # Output: 0
