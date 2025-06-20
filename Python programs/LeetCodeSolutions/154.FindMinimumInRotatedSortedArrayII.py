"""
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element. The array may contain duplicates.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- nums is sorted and rotated.

Example:
Input: nums = [2,2,2,0,1]
Output: 0
"""
from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    return nums[left]

# Example usage:
if __name__ == "__main__":
    print(findMin([2,2,2,0,1]))  # Output: 0
    print(findMin([1,3,5]))      # Output: 1
