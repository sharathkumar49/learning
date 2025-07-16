"""
LeetCode 2292. Products of the Maximum Product of Two Elements

Given nums, return the maximum product of two elements minus one.

Example:
Input: nums = [3,4,5,2]
Output: 14

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 1000
"""

def maxProduct(nums):
    nums.sort()
    return (nums[-1]-1)*(nums[-2]-1)

# Example usage:
# print(maxProduct([3,4,5,2]))  # Output: 14
