"""
LeetCode 2216. Minimum Deletions to Make Array Beautiful

Given an array nums, return the minimum deletions to make the array beautiful.

Example:
Input: nums = [1,1,2,3,5]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def minDeletion(nums):
    res = 0
    i = 0
    while i < len(nums):
        if i%2 == 1 and nums[i] == nums[i-1]:
            res += 1
            nums.pop(i)
        else:
            i += 1
    if len(nums)%2:
        res += 1
    return res

# Example usage:
# print(minDeletion([1,1,2,3,5]))  # Output: 1
