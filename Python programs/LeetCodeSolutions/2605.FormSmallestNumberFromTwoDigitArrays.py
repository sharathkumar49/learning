"""
LeetCode 2605. Form Smallest Number From Two Digit Arrays

Given two digit arrays, return the smallest number formed.

Constraints:
- 1 <= nums1.length, nums2.length <= 9
"""

def minNumber(nums1, nums2):
    s1, s2 = set(nums1), set(nums2)
    common = s1 & s2
    if common:
        return min(common)
    return min(min(nums1)*10+min(nums2), min(nums2)*10+min(nums1))
# Example usage:
# print(minNumber([4,1,3],[5,7]))  # Output: 15
