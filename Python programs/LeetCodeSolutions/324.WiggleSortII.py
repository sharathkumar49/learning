"""
324. Wiggle Sort II

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 5000
- It is guaranteed that there will be an answer for the given input nums.
"""
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]
        nums[::2] = small
        nums[1::2] = large

# Example usage:
nums = [1,5,1,1,6,4]
Solution().wiggleSort(nums)
print(nums)  # Output: [1,6,1,5,1,4] or any valid wiggle sort
