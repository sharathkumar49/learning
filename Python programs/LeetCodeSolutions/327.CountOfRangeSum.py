"""
327. Count of Range Sum

Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

A range sum is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- -2^31 <= lower <= upper <= 2^31 - 1
"""
from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            j = k = t = mid
            cache = []
            for left in pre[lo:mid]:
                while k < hi and pre[k] - left < lower:
                    k += 1
                while j < hi and pre[j] - left <= upper:
                    j += 1
                count += j - k
            pre[lo:hi] = sorted(pre[lo:hi])
            return count
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        return sort(0, len(pre))

# Example usage:
nums = [-2,5,-1]
lower = -2
upper = 2
print(Solution().countRangeSum(nums, lower, upper))  # Output: 3
