"""
LeetCode 1920. Build Array from Permutation

Given a zero-based permutation nums, build an array ans where ans[i] = nums[nums[i]].

Example:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] < nums.length
"""

def buildArray(nums):
    return [nums[nums[i]] for i in range(len(nums))]

# Example usage:
# print(buildArray([0,2,1,5,3,4]))  # Output: [0,1,2,4,5,3]
