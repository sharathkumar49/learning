"""
LeetCode 1818. Minimum Absolute Sum Difference

Given two arrays nums1 and nums2, return the minimum absolute sum difference after replacing at most one element in nums1.

Example 1:
Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3

Constraints:
- 1 <= nums1.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^5
"""

def minAbsoluteSumDiff(nums1, nums2):
    import bisect
    MOD = 10**9+7
    arr = sorted(nums1)
    res = 0
    gain = 0
    for a, b in zip(nums1, nums2):
        diff = abs(a-b)
        res += diff
        idx = bisect.bisect_left(arr, b)
        if idx < len(arr):
            gain = max(gain, diff - abs(arr[idx]-b))
        if idx > 0:
            gain = max(gain, diff - abs(arr[idx-1]-b))
    return (res - gain) % MOD

# Example usage:
# nums1 = [1,7,5]
# nums2 = [2,3,5]
# print(minAbsoluteSumDiff(nums1, nums2))  # Output: 3
