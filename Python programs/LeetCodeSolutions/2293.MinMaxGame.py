"""
LeetCode 2293. Min Max Game

Given nums, return the result of the min-max game.

Example:
Input: nums = [1,3,5,2,4,8,2,2]
Output: 1

Constraints:
- 1 <= nums.length <= 1000
- nums.length is a power of 2
"""

def minMaxGame(nums):
    while len(nums) > 1:
        nums = [min(nums[i], nums[i+1]) if i%2==0 else max(nums[i], nums[i+1]) for i in range(0, len(nums)-1, 2)]
    return nums[0]

# Example usage:
# print(minMaxGame([1,3,5,2,4,8,2,2]))  # Output: 1
