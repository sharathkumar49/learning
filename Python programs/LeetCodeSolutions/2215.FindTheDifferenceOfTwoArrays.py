"""
LeetCode 2215. Find the Difference of Two Arrays

Given two arrays nums1 and nums2, return their distinct elements as two lists.

Example:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 1 <= nums1[i], nums2[i] <= 1000
"""

def findDifference(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    return [list(set1-set2), list(set2-set1)]

# Example usage:
# print(findDifference([1,2,3], [2,4,6]))  # Output: [[1,3],[4,6]]
