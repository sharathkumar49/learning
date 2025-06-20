"""
89. Gray Code
https://leetcode.com/problems/gray-code/

Given an integer n, return any sequence of 2^n integers such that every integer appears exactly once, and that every two consecutive integers differ by exactly one bit in their binary representation.

Constraints:
- 1 <= n <= 16

Example:
Input: n = 2
Output: [0,1,3,2]
"""
from typing import List

def grayCode(n: int) -> List[int]:
    res = [0]
    for i in range(n):
        res += [x | 1 << i for x in reversed(res)]
    return res

# Example usage:
if __name__ == "__main__":
    print(grayCode(2))  # Output: [0, 1, 3, 2]
    print(grayCode(3))  # Output: [0, 1, 3, 2, 6, 7, 5, 4]
