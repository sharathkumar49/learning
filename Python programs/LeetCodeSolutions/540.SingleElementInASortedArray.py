"""
540. Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once, return the single element that appears only once.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5

Example:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""

class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

# Example usage:
sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Output: 2
