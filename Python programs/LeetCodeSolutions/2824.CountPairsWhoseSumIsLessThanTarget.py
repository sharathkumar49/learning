"""
LeetCode 2824. Count Pairs Whose Sum is Less than Target

Given nums and target, return the number of pairs whose sum is less than target.

Constraints:
- 2 <= nums.length <= 50
"""

def countPairs(nums, target):
    nums.sort()
    count = 0
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count
# Example usage:
# print(countPairs([1,2,3,4], 5))  # Output: 2
