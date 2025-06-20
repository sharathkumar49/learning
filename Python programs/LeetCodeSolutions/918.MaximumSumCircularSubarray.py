"""
918. Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array.

Constraints:
- n == nums.length
- 1 <= n <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4

Example:
Input: nums = [1,-2,3,-2]
Output: 3
"""
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_max = cur_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        for x in nums:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)

# Example usage
if __name__ == "__main__":
    nums = [1,-2,3,-2]
    print(Solution().maxSubarraySumCircular(nums))  # Output: 3
