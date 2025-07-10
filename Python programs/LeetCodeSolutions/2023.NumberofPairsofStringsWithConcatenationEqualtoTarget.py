"""
LeetCode 2023. Number of Pairs of Strings With Concatenation Equal to Target

Given an array of strings nums and a string target, return the number of pairs of indices (i, j) such that i != j and nums[i] + nums[j] == target.

Example:
Input: nums = ["777","7","77","77"], target = "7777"
Output: 4

Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i].length <= 100
- 1 <= target.length <= 100
"""

def numOfPairs(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                count += 1
    return count

# Example usage:
# print(numOfPairs(["777","7","77","77"], "7777"))  # Output: 4
