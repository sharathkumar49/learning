# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
#
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
#
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
nums = [-1,0,3,5,9,12]
target = 9
print("Index of target:", search(nums, target))  # Output: 4
