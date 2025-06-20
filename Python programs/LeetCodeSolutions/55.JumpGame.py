# 55. Jump Game
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
#
# Constraints:
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

def canJump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

# Example usage
nums = [2,3,1,1,4]
print("Can jump:", canJump(nums))  # Output: True
