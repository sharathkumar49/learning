"""
LeetCode 2535. Difference Between Element Sum and Digit Sum of an Array

Given an array, return the difference between element sum and digit sum.

Constraints:
- 1 <= nums.length <= 2000
"""

def differenceOfSum(nums):
    return sum(nums) - sum(int(d) for x in nums for d in str(x))
# Example usage:
# print(differenceOfSum([1,15,6,3]))  # Output: 9
