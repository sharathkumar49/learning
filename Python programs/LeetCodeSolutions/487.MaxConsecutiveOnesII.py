"""
487. Max Consecutive Ones II

Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Example:
Input: nums = [1,0,1,1,0]
Output: 4
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max_count = 0
        left = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_count = max(max_count, right - left + 1)
        return max_count

# Example usage:
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,1,0]))  # Output: 4
