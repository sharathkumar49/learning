"""
413. Arithmetic Slices

Given an integer array nums, return the number of arithmetic subarrays of length at least 3.

Constraints:
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000
"""
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = curr = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                res += curr
            else:
                curr = 0
        return res

# Example usage:
nums = [1,2,3,4]
print(Solution().numberOfArithmeticSlices(nums))  # Output: 3
