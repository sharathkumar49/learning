"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Constraints:
- 1 <= nums.length <= 300
- nums[i] is 0, 1, or 2.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
from typing import List

def sortColors(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage:
if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    sortColors(arr)
    print(arr)  # Output: [0,0,1,1,2,2]
