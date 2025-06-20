"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Find the minimum element.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.

Example:
Input: nums = [3,4,5,1,2]
Output: 1
"""
from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Example usage:
if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))  # Output: 1
    print(findMin([4,5,6,7,0,1,2]))  # Output: 0
