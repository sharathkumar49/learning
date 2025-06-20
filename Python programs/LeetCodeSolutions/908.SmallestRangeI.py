"""
908. Smallest Range I
https://leetcode.com/problems/smallest-range-i/

Given an array nums and an integer k, modify the array by adding or subtracting k to each element. Return the smallest possible difference between the maximum and minimum of the array after modification.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^4
- 0 <= k <= 10^4

Example:
Input: nums = [1], k = 0
Output: 0
"""
from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)

# Example usage
if __name__ == "__main__":
    nums = [1]
    k = 0
    print(Solution().smallestRangeI(nums, k))  # Output: 0
