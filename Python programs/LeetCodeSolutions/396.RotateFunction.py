"""
396. Rotate Function

Given an integer array nums, return the maximum value of F(0), F(1), ..., F(n-1), where F(k) is the rotate function defined as:
F(k) = 0 * nums[k % n] + 1 * nums[(k+1) % n] + ... + (n-1) * nums[(k+n-1) % n]

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- -10^9 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        res = f
        for i in range(1, n):
            f = f + total - n * nums[-i]
            res = max(res, f)
        return res

# Example usage:
nums = [4,3,2,6]
print(Solution().maxRotateFunction(nums))  # Output: 26
