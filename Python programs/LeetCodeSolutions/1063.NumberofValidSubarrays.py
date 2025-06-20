"""
1063. Number of Valid Subarrays

Given an array of integers nums, return the number of valid subarrays. A valid subarray is a contiguous subarray where the leftmost element is not larger than any other element in the subarray.

Constraints:
- 1 <= nums.length <= 50,000
- 0 <= nums[i] < nums.length

Example:
Input: nums = [1,4,2,5,3]
Output: 11
"""
from typing import List

def validSubarrays(nums: List[int]) -> int:
    stack = []
    res = 0
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] > num:
            stack.pop()
        stack.append(i)
    prev = -1
    for i in stack:
        res += i - prev
        prev = i
    return res

# Example usage:
nums = [1,4,2,5,3]
print(validSubarrays(nums))  # Output: 11
