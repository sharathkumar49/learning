"""
801. Minimum Swaps To Make Sequences Increasing

Given two integer arrays nums1 and nums2 of the same length, you are allowed to swap elements at the same index. Return the minimum number of swaps needed to make both sequences strictly increasing.

Example 1:
Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1

Example 2:
Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
Output: 1

Constraints:
- 2 <= nums1.length <= 10^5
- nums1.length == nums2.length
- 0 <= nums1[i], nums2[i] <= 2 * 10^5
"""
def minSwap(nums1, nums2):
    n = len(nums1)
    keep = [float('inf')] * n
    swap = [float('inf')] * n
    keep[0] = 0
    swap[0] = 1
    for i in range(1, n):
        if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
            keep[i] = keep[i-1]
            swap[i] = swap[i-1] + 1
        if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
            keep[i] = min(keep[i], swap[i-1])
            swap[i] = min(swap[i], keep[i-1] + 1)
    return min(keep[-1], swap[-1])

# Example usage:
print(minSwap([1,3,5,4], [1,2,3,7]))  # Output: 1
print(minSwap([0,3,5,8,9], [2,1,4,6,9]))  # Output: 1
