"""
LeetCode 1537. Get the Maximum Score

Given two sorted arrays nums1 and nums2, return the maximum sum you can obtain by traversing through the arrays as described in the problem statement.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^7

Example:
Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
"""
def maxSum(nums1, nums2):
    mod = 10**9 + 7
    i = j = 0
    s1 = s2 = 0
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]):
            s1 += nums1[i]
            i += 1
        elif j < len(nums2) and (i == len(nums1) or nums1[i] > nums2[j]):
            s2 += nums2[j]
            j += 1
        else:
            s1 = s2 = max(s1, s2) + nums1[i]
            i += 1
            j += 1
    return max(s1, s2) % mod

# Example usage:
nums1 = [2,4,5,8,10]
nums2 = [4,6,8,9]
print(maxSum(nums1, nums2))  # Output: 30
