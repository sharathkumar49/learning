"""
LeetCode 1855. Maximum Distance Between a Pair of Values

You are given two non-increasing integer arrays nums1 and nums2. Return the maximum distance j - i such that i <= j and nums1[i] <= nums2[j].

Example 1:
Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[j] <= 10^5
"""

def maxDistance(nums1, nums2):
    ans = 0
    i = 0
    for j in range(len(nums2)):
        while i < len(nums1) and nums1[i] > nums2[j]:
            i += 1
        if i < len(nums1):
            ans = max(ans, j - i)
    return ans

# Example usage:
# nums1 = [55,30,5,4,2]
# nums2 = [100,20,10,10,5]
# print(maxDistance(nums1, nums2))  # Output: 2
