"""
454. 4Sum II

Given four integer arrays nums1, nums2, nums3, nums4 all of length n, return the number of tuples (i, j, k, l) such that:
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Constraints:
- n == nums1.length == nums2.length == nums3.length == nums4.length
- 1 <= n <= 200
- -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28

Example:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
"""

from collections import Counter

class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        count = Counter(a + b for a in nums1 for b in nums2)
        return sum(count[-(c + d)] for c in nums3 for d in nums4)

# Example usage:
sol = Solution()
print(sol.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))  # Output: 2
