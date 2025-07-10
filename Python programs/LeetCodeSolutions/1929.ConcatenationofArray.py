"""
LeetCode 1929. Concatenation of Array

Given an integer array nums, return the concatenation of nums with itself.

Example:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def getConcatenation(nums):
    return nums + nums

# Example usage:
# print(getConcatenation([1,2,1]))  # Output: [1,2,1,1,2,1]
