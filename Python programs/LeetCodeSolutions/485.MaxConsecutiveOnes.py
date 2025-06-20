"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

# Example usage:
sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
