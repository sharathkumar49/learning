"""
LeetCode 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers

Given two arrays of integers `nums1` and `nums2`, return the number of triplets `(i, j, k)` such that:
- `0 <= i < nums1.length`
- `0 <= j < k < nums2.length`
- `nums1[i]^2 == nums2[j] * nums2[k]`

Or, the number of triplets `(i, j, k)` such that:
- `0 <= i < nums2.length`
- `0 <= j < k < nums1.length`
- `nums2[i]^2 == nums1[j] * nums1[k]`

Example 1:
Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: (1, 1, 2) is valid because 4^2 = 2 * 8 = 16

Example 2:
Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All triplets are valid.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 1 <= nums1[i], nums2[i] <= 10^5
"""

from collections import Counter

def numTriplets(nums1, nums2):
    def count(a, b):
        res = 0
        cnt = Counter(b)
        for x in a:
            target = x * x
            for y in cnt:
                if target % y == 0:
                    z = target // y
                    if z in cnt:
                        if y == z:
                            res += cnt[y] * (cnt[y] - 1) // 2
                        elif y < z:
                            res += cnt[y] * cnt[z]
        return res
    return count(nums1, nums2) + count(nums2, nums1)
