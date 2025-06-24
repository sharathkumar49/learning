"""
LeetCode 1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, return the minimum value to start with so that the step by step sum is always positive.

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100

Example:
Input: nums = [-3,2,-3,4,2]
Output: 5
"""
def minStartValue(nums):
    total = 0
    min_sum = 0
    for n in nums:
        total += n
        min_sum = min(min_sum, total)
    return 1 - min_sum

# Example usage:
nums = [-3,2,-3,4,2]
print(minStartValue(nums))  # Output: 5
