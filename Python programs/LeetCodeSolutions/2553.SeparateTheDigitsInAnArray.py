"""
LeetCode 2553. Separate the Digits in an Array

Given an array, return an array with all digits separated.

Constraints:
- 1 <= nums.length <= 10^5
"""

def separateDigits(nums):
    return [int(d) for x in nums for d in str(x)]
# Example usage:
# print(separateDigits([13,25,83,77]))  # Output: [1,3,2,5,8,3,7,7]
