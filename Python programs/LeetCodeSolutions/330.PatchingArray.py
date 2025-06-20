"""
330. Patching Array

Given a sorted array of positive integers nums and an integer n, add the minimum number of patches (numbers) to the array so that every number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- 1 <= n <= 2^31 - 1
"""
from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, i, added = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added

# Example usage:
nums = [1,3]
n = 6
print(Solution().minPatches(nums, n))  # Output: 1
