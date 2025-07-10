"""
LeetCode 2057. Smallest Index With Equal Value

Given an array nums, return the smallest index i such that nums[i] == i. If no such index exists, return -1.

Example:
Input: nums = [0,2,3,4,5]
Output: 0

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

def smallestEqual(nums):
    for i, x in enumerate(nums):
        if i % 10 == x:
            return i
    return -1

# Example usage:
# print(smallestEqual([0,2,3,4,5]))  # Output: 0
