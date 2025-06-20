"""
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values). Given the array and an integer target, return true if target is in nums, or false otherwise.

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i], target <= 10^4

Example:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
"""
from typing import List

def search(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False

# Example usage:
if __name__ == "__main__":
    print(search([2,5,6,0,0,1,2], 0))  # Output: True
    print(search([2,5,6,0,0,1,2], 3))  # Output: False
