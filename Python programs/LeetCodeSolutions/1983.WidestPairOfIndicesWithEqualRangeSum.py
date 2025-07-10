"""
LeetCode 1983. Widest Pair of Indices With Equal Range Sum

Given two integer arrays nums1 and nums2, return the widest pair of indices (i, j) such that the sum of nums1[i..j] equals the sum of nums2[i..j].

Example:
Input: nums1 = [1,2,3,4], nums2 = [2,2,3,4]
Output: 2

Constraints:
- 1 <= nums1.length == nums2.length <= 10^5
- -10^5 <= nums1[i], nums2[i] <= 10^5
"""

def widestPairOfIndices(nums1, nums2):
    diff = {0: -1}
    s1 = s2 = res = 0
    for i, (a, b) in enumerate(zip(nums1, nums2)):
        s1 += a
        s2 += b
        d = s1 - s2
        if d in diff:
            res = max(res, i - diff[d])
        else:
            diff[d] = i
    return res

# Example usage:
# print(widestPairOfIndices([1,2,3,4], [2,2,3,4]))  # Output: 2
