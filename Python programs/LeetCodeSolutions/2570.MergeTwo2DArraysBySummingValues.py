"""
LeetCode 2570. Merge Two 2D Arrays by Summing Values

Given two 2D arrays, merge them by summing values.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
"""

def mergeArrays(nums1, nums2):
    from collections import defaultdict
    d = defaultdict(int)
    for k,v in nums1+nums2:
        d[k] += v
    return sorted(d.items())
# Example usage:
# print(mergeArrays([[1,2],[2,3]], [[2,4],[3,5]]))  # Output: [[1,2],[2,7],[3,5]]
