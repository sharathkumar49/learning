"""
LeetCode 2040. Kth Smallest Product of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 and an integer k, return the k-th smallest product of nums1[i] * nums2[j].

Example:
Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8

Constraints:
- 1 <= nums1.length, nums2.length <= 5 * 10^4
- -10^5 <= nums1[i], nums2[i] <= 10^5
- 1 <= k <= nums1.length * nums2.length
"""

def kthSmallestProduct(nums1, nums2, k):
    def count_leq(x):
        cnt = 0
        for a in nums1:
            if a >= 0:
                l, r = 0, len(nums2)
                while l < r:
                    m = (l + r) // 2
                    if a * nums2[m] <= x:
                        l = m + 1
                    else:
                        r = m
                cnt += l
            else:
                l, r = 0, len(nums2)
                while l < r:
                    m = (l + r) // 2
                    if a * nums2[m] <= x:
                        r = m
                    else:
                        l = m + 1
                cnt += len(nums2) - l
        return cnt
    left, right = -10**10, 10**10
    while left < right:
        mid = (left + right) // 2
        if count_leq(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage:
# print(kthSmallestProduct([2,5], [3,4], 2))  # Output: 8
