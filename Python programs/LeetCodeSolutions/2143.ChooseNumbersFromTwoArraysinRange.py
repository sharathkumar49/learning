"""
LeetCode 2143. Choose Numbers From Two Arrays in Range

Given two integer arrays nums1 and nums2, and two integers l and r, return the number of pairs (i, j) such that nums1[i] + nums2[j] is in the range [l, r].

Example:
Input: nums1 = [1,2,3], nums2 = [3,4], l = 4, r = 6
Output: 4
Explanation: The pairs are (1,3), (1,4), (2,3), (3,4).

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- -10^9 <= nums1[i], nums2[j], l, r <= 10^9
"""

def countPairs(nums1, nums2, l, r):
    from bisect import bisect_left, bisect_right
    nums2.sort()
    res = 0
    for a in nums1:
        left = l - a
        right = r - a
        res += bisect_right(nums2, right) - bisect_left(nums2, left)
    return res

# Example usage:
# print(countPairs([1,2,3], [3,4], 4, 6))  # Output: 4
