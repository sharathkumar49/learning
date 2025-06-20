"""
410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, split the array into m non-empty continuous subarrays. Minimize the largest sum among these subarrays.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^6
- 1 <= m <= min(50, nums.length)
"""
from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            total, count = 0, 1
            for num in nums:
                if total + num > mid:
                    total = num
                    count += 1
                else:
                    total += num
            if count > m:
                left = mid + 1
            else:
                right = mid
        return left

# Example usage:
nums = [7,2,5,10,8]
m = 2
print(Solution().splitArray(nums, m))  # Output: 18
