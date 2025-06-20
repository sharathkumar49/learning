"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n

Example:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i+1 for i, num in enumerate(nums) if num > 0]

# Example usage:
sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5, 6]
