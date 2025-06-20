"""
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. Return the new length.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.

Example:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
"""
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    return i

# Example usage:
if __name__ == "__main__":
    arr = [1,1,1,2,2,3]
    k = removeDuplicates(arr)
    print(k, arr[:k])  # Output: 5 [1,1,2,2,3]
