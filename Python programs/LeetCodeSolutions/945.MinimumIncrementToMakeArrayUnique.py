"""
945. Minimum Increment to Make Array Unique
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

Given an integer array nums, return the minimum number of increments to make every element in the array unique.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5

Example:
Input: nums = [3,2,1,2,1,7]
Output: 6
"""
from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                res += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return res

# Example usage
if __name__ == "__main__":
    nums = [3,2,1,2,1,7]
    print(Solution().minIncrementForUnique(nums))  # Output: 6
