"""
325. Maximum Size Subarray Sum Equals k

Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Constraints:
- 1 <= nums.length <= 2 * 10^5
- -10^4 <= nums[i] <= 10^4
- -10^9 <= k <= 10^9
"""
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = {0: -1}
        total = 0
        res = 0
        for i, num in enumerate(nums):
            total += num
            if total - k in prefix:
                res = max(res, i - prefix[total - k])
            if total not in prefix:
                prefix[total] = i
        return res

# Example usage:
nums = [1, -1, 5, -2, 3]
k = 3
print(Solution().maxSubArrayLen(nums, k))  # Output: 4
