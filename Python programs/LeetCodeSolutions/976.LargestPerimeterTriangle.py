"""
976. Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of non-zero area, return 0.

Constraints:
- 3 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^6

Example:
Input: nums = [2,1,2]
Output: 5
"""
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# Example usage
if __name__ == "__main__":
    nums = [2,1,2]
    print(Solution().largestPerimeter(nums))  # Output: 5
