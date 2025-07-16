"""
LeetCode 2239. Find Closest Number to Zero

Given an array nums, return the number closest to zero. If there is a tie, return the larger number.

Example:
Input: nums = [-4,-2,1,4]
Output: 1

Constraints:
- 1 <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5
"""

def findClosestNumber(nums):
    return max([x for x in nums if abs(x) == min(abs(y) for y in nums)])

# Example usage:
# print(findClosestNumber([-4,-2,1,4]))  # Output: 1
