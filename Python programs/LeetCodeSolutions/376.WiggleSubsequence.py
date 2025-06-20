"""
376. Wiggle Subsequence

Given an integer array nums, return the length of the longest wiggle subsequence. A wiggle sequence is one where the differences between successive numbers strictly alternate between positive and negative.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)

# Example usage:
nums = [1,7,4,9,2,5]
print(Solution().wiggleMaxLength(nums))  # Output: 6
