"""
421. Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Constraints:
- 1 <= nums.length <= 2 * 10^5
- 0 <= nums[i] <= 2^31 - 1
"""
from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            found = set([num & mask for num in nums])
            temp = res | (1 << i)
            if any(temp ^ f in found for f in found):
                res = temp
        return res

# Example usage:
nums = [3,10,5,25,2,8]
print(Solution().findMaximumXOR(nums))  # Output: 28
