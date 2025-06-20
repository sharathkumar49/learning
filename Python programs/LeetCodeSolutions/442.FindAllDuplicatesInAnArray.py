"""
442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n

Example:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
"""

class Solution:
    def findDuplicates(self, nums: list) -> list:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return res

# Example usage:
sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Output: [2, 3]
