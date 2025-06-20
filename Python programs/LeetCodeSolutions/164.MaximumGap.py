"""
164. Maximum Gap
https://leetcode.com/problems/maximum-gap/

Given an integer array nums, return the maximum difference between the successive elements in its sorted form. If the array contains less than two elements, return 0.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9

Example:
Input: nums = [3,6,9,1]
Output: 3
"""
from typing import List

def maximumGap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    nums.sort()
    return max(nums[i] - nums[i-1] for i in range(1, len(nums)))

# Example usage:
if __name__ == "__main__":
    print(maximumGap([3,6,9,1]))  # Output: 3
    print(maximumGap([10]))       # Output: 0
