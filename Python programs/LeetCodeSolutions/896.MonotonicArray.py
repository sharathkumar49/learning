"""
896. Monotonic Array
https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5

Example:
Input: nums = [1,2,2,3]
Output: true
"""
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            if nums[i] < nums[i-1]:
                increasing = False
        return increasing or decreasing

# Example usage
if __name__ == "__main__":
    nums = [1,2,2,3]
    print(Solution().isMonotonic(nums))  # Output: True
