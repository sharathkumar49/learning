"""
532. K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where i != j and |nums[i] - nums[j]| == k.

Constraints:
- 1 <= nums.length <= 10^4
- -10^7 <= nums[i] <= 10^7
- 0 <= k <= 10^7

Example:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
"""

class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        if k < 0:
            return 0
        seen = set(nums)
        if k == 0:
            from collections import Counter
            return sum(v > 1 for v in Counter(nums).values())
        return sum(num + k in seen for num in seen)

# Example usage:
sol = Solution()
print(sol.findPairs([3,1,4,1,5], 2))  # Output: 2
