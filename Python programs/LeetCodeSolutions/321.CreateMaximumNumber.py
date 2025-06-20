"""
321. Create Maximum Number

You are given two integer arrays nums1 and nums2 of lengths m and n respectively. Return an array of the maximum number of length k <= m + n formed from digits of the two arrays. The relative order of the digits from the same array must be preserved.

Constraints:
- m == nums1.length
- n == nums2.length
- 1 <= m, n <= 500
- 0 <= nums1[i], nums2[i] <= 9
- 1 <= k <= m + n
"""
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums, t):
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]
        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
        return max(merge(pick_max(nums1, i), pick_max(nums2, k - i))
                   for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1))

# Example usage:
nums1 = [3,4,6,5]
nums2 = [9,1,2,5,8,3]
k = 5
print(Solution().maxNumber(nums1, nums2, k))  # Output: [9,8,6,5,3]
