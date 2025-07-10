"""
LeetCode 1822. Sign of the Product of an Array

Given an integer array nums, return 1 if the product is positive, -1 if negative, 0 if zero.

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1

Constraints:
- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100
"""

def arraySign(nums):
    sign = 1
    for x in nums:
        if x == 0:
            return 0
        if x < 0:
            sign = -sign
    return sign

# Example usage:
# nums = [-1,-2,-3,-4,3,2,1]
# print(arraySign(nums))  # Output: 1
