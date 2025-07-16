"""
LeetCode 2321. Maximum Score of Spliced Array

Given nums1 and nums2, return the maximum score after splicing.

Example:
Input: nums1 = [60,60,60], nums2 = [10,90,10]
Output: 210

Constraints:
- 1 <= nums1.length == nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^4
"""

def maximumsSplicedArray(nums1, nums2):
    def maxDiff(a, b):
        diff = [x-y for x, y in zip(a, b)]
        curr = res = 0
        for d in diff:
            curr = max(d, curr+d)
            res = max(res, curr)
        return res
    return max(sum(nums1)+maxDiff(nums2, nums1), sum(nums2)+maxDiff(nums1, nums2))

# Example usage:
# print(maximumsSplicedArray([60,60,60], [10,90,10]))  # Output: 210
