"""
LeetCode 1979. Find Greatest Common Divisor of Array

Given an integer array nums, return the greatest common divisor of the smallest and largest number in nums.

Example:
Input: nums = [2,5,6,9,10]
Output: 2

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def findGCD(nums):
    from math import gcd
    return gcd(min(nums), max(nums))

# Example usage:
# print(findGCD([2,5,6,9,10]))  # Output: 2
