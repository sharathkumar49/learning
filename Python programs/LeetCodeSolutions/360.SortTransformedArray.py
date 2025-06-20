"""
360. Sort Transformed Array

Given a sorted array of integers nums and integer values a, b, and c, apply a quadratic function of the form f(x) = ax^2 + bx + c to each element x in nums, and return the resulting array in sorted order.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -100 <= nums[i] <= 100
- -100 <= a, b, c <= 100
- nums is sorted in ascending order.
"""
from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x):
            return a * x * x + b * x + c
        n = len(nums)
        res = [0] * n
        i, j = 0, n - 1
        idx = n - 1 if a >= 0 else 0
        while i <= j:
            left, right = f(nums[i]), f(nums[j])
            if a >= 0:
                if left > right:
                    res[idx] = left
                    i += 1
                else:
                    res[idx] = right
                    j -= 1
                idx -= 1
            else:
                if left < right:
                    res[idx] = left
                    i += 1
                else:
                    res[idx] = right
                    j -= 1
                idx += 1
        return res

# Example usage:
nums = [-4,-2,2,4]
a, b, c = 1, 3, 5
print(Solution().sortTransformedArray(nums, a, b, c))  # Output: [3,9,15,33]
