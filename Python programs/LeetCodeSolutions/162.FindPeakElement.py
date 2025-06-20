"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i+1] for all valid i

Example:
Input: nums = [1,2,3,1]
Output: 2
"""
from typing import List

def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left

# Example usage:
if __name__ == "__main__":
    print(findPeakElement([1,2,3,1]))  # Output: 2
    print(findPeakElement([1,2,1,3,5,6,4]))  # Output: 5
