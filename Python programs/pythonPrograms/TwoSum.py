# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
#
# Example 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
#
# Example 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, x in enumerate(nums):
            if (y := target - x) in d:
                return [d[y], i]
            d[x] = i

print(Solution().twoSum([1, 7, 2, 4, 13], 11))
print(Solution().twoSum([5, 2, 1, 8, 13], 6))
