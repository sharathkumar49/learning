"""
970. Powerful Integers
https://leetcode.com/problems/powerful-integers/

Given two non-negative integers x and y, and an integer bound, return a list of all powerful integers that have the value less than or equal to bound.
An integer is powerful if it can be represented as x^i + y^j for some integers i >= 0 and j >= 0.

Constraints:
- 1 <= x, y <= 100
- 0 <= bound <= 10^6

Example:
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
"""
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        i = 1
        while i <= bound:
            j = 1
            while i + j <= bound:
                res.add(i + j)
                if y == 1:
                    break
                j *= y
            if x == 1:
                break
            i *= x
        return list(res)

# Example usage
if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    print(sorted(Solution().powerfulIntegers(x, y, bound)))  # Output: [2,3,4,5,7,9,10]
