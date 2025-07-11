# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# Example usage
nums = [1,2,3,1]
print("Contains duplicate:", containsDuplicate(nums))  # Output: True
