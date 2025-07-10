"""
LeetCode 1748. Sum of Unique Elements

Given an array nums, return the sum of all unique elements.

Example 1:
Input: nums = [1,2,3,2]
Output: 4

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def sumOfUnique(nums):
    from collections import Counter
    count = Counter(nums)
    return sum(x for x, c in count.items() if c == 1)

# Example usage:
# nums = [1,2,3,2]
# print(sumOfUnique(nums))  # Output: 4
