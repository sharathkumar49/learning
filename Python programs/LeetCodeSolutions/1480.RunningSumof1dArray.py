"""
LeetCode 1480. Running Sum of 1d Array

Given an array nums, return the running sum of nums.

Constraints:
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6

Example:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
"""
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

# Example usage:
nums = [1,2,3,4]
print(runningSum(nums))  # Output: [1, 3, 6, 10]
