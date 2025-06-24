"""
LeetCode 1295. Find Numbers with Even Number of Digits

Given an array nums, return how many of them contain an even number of digits.

Constraints:
- 1 <= nums.length <= 500
- 1 <= nums[i] <= 10^5

Example:
Input: nums = [12,345,2,6,7896]
Output: 2
"""
def findNumbers(nums):
    return sum(1 for x in nums if len(str(x)) % 2 == 0)

# Example usage:
nums = [12,345,2,6,7896]
print(findNumbers(nums))  # Output: 2
