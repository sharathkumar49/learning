"""
LeetCode 2089. Find Target Indices After Sorting Array

Given an array nums and an integer target, return the indices of target after sorting nums.

Example:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i], target <= 100
"""

def targetIndices(nums, target):
    nums.sort()
    return [i for i, x in enumerate(nums) if x == target]

# Example usage:
# print(targetIndices([1,2,5,2,3], 2))  # Output: [1,2]
