"""
LeetCode 2540. Minimum Common Value

Given two sorted arrays, return the minimum common value.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
"""

def getCommon(nums1, nums2):
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1
# Example usage:
# print(getCommon([1,2,3],[2,4]))  # Output: 2
