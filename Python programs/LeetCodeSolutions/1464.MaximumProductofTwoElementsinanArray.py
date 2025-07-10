"""
LeetCode 1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, return the maximum value of (nums[i]-1)*(nums[j]-1) where i and j are different indices.

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^3

Example:
Input: nums = [3,4,5,2]
Output: 12
"""
def maxProduct(nums):
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)

# Example usage:
nums = [3,4,5,2]
print(maxProduct(nums))  # Output: 12
