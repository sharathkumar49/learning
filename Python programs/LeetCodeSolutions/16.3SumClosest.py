# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
#
# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
#
# Constraints:
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4

def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return s
    return closest

# Example usage
nums = [-1,2,1,-4]
target = 1
print("3Sum Closest:", threeSumClosest(nums, target))  # Output: 2
