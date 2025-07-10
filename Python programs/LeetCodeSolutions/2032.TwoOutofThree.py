"""
LeetCode 2032. Two Out of Three

Given three integer arrays nums1, nums2, and nums3, return a list of all numbers that are present in at least two out of the three arrays.

Example:
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]

Constraints:
- 1 <= nums1.length, nums2.length, nums3.length <= 100
- 1 <= nums1[i], nums2[i], nums3[i] <= 100
"""

def twoOutOfThree(nums1, nums2, nums3):
    sets = [set(nums1), set(nums2), set(nums3)]
    res = set()
    for i in range(3):
        for j in range(i+1, 3):
            res |= sets[i] & sets[j]
    return list(res)

# Example usage:
# print(twoOutOfThree([1,1,3,2], [2,3], [3]))  # Output: [3,2]
