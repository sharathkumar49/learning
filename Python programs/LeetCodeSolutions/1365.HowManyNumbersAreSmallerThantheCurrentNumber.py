"""
LeetCode 1365. How Many Numbers Are Smaller Than the Current Number

Given an array nums, return an array answer such that answer[i] is the number of numbers smaller than nums[i].

Constraints:
- 2 <= nums.length <= 500
- 0 <= nums[i] <= 100

Example:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
"""
def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    return [sorted_nums.index(x) for x in nums]

# Example usage:
nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))  # Output: [4,0,1,1,3]
