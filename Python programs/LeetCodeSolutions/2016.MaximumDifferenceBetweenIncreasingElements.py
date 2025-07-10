"""
LeetCode 2016. Maximum Difference Between Increasing Elements

Given a 0-indexed integer array nums, return the maximum difference between two elements such that the larger element comes after the smaller one.

Example:
Input: nums = [7,1,5,4]
Output: 4

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
"""

def maximumDifference(nums):
    min_num = nums[0]
    res = -1
    for num in nums[1:]:
        if num > min_num:
            res = max(res, num - min_num)
        min_num = min(min_num, num)
    return res

# Example usage:
# print(maximumDifference([7,1,5,4]))  # Output: 4
