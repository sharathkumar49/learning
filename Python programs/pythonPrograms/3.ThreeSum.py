# Given an array of integers nums and an integer target,
# return all unique triplets [i, j, k] such that they add up to target.
#
# You may not use the same element twice in a triplet.
#
# Example:
# Input: nums = [1, 2, -2, 0, -1, 1], target = 0
# Output: [[-2, 1, 1], [-1, 0, 1]]
#
# Constraints:
# 3 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

class Solution:
    def threeSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res

print(Solution().threeSum([1, 2, -2, 0, -1, 1], 0))
print(Solution().threeSum([0, 0, 0, 0], 0))
print(Solution().threeSum([3, -1, -1, 0, 2, -2, 1], 2))
