# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Return k after placing the final result in the first k slots of nums.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
#
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#
# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k

# Example usage
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print("After removing duplicates:", nums[:k])  # Output: [0,1,2,3,4]
