"""
LeetCode 2148. Count Elements With Strictly Smaller and Greater Elements

Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element.

Example:
Input: nums = [11,7,2,15]
Output: 2

Constraints:
- 1 <= nums.length <= 100
- -10^5 <= nums[i] <= 10^5
"""

def countElements(nums):
    mn, mx = min(nums), max(nums)
    return sum(mn < x < mx for x in nums)

# Example usage:
# print(countElements([11,7,2,15]))  # Output: 2
