"""
LeetCode 1885. Count Pairs in Two Arrays

Given two integer arrays nums1 and nums2, and an integer diff, return the number of pairs (i, j) such that nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff and i < j.

Example:
Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
Output: 3

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- -10^4 <= nums1[i], nums2[i] <= 10^4
- -10^4 <= diff <= 10^4
"""

def countPairs(nums1, nums2, diff):
    arr = [a - b for a, b in zip(nums1, nums2)]
    res = 0
    from bisect import bisect_right, insort
    sorted_arr = []
    for a in arr:
        res += bisect_right(sorted_arr, a + diff)
        insort(sorted_arr, a)
    return res

# Example usage:
# print(countPairs([3,2,5], [2,2,1], 1))  # Output: 3
