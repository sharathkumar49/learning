# 45. Jump Game II
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Return the minimum number of jumps to reach the last index.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
#
# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000

def jump(nums):
    jumps = 0
    cur_end = cur_farthest = 0
    for i in range(len(nums) - 1):
        cur_farthest = max(cur_farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_farthest
    return jumps

# Example usage
nums = [2,3,1,1,4]
print("Minimum jumps:", jump(nums))  # Output: 2
