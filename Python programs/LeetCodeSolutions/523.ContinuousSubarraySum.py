"""
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums[i]) <= 2^31 - 1
- 1 <= k <= 2^31 - 1

Example:
Input: nums = [23,2,4,6,7], k = 6
Output: true
"""

class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        mod_map = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            mod = total % k if k != 0 else total
            if mod in mod_map:
                if i - mod_map[mod] > 1:
                    return True
            else:
                mod_map[mod] = i
        return False

# Example usage:
sol = Solution()
print(sol.checkSubarraySum([23,2,4,6,7], 6))  # Output: True
