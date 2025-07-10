"""
LeetCode 1458. Max Dot Product of Two Subsequences

Given two arrays nums1 and nums2, return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

Constraints:
- 1 <= nums1.length, nums2.length <= 500
- -1000 <= nums1[i], nums2[i] <= 1000

Example:
Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
"""
def maxDotProduct(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prod = nums1[i] * nums2[j]
            dp[i+1][j+1] = max(prod, dp[i][j] + prod, dp[i][j+1], dp[i+1][j])
    return dp[m][n]

# Example usage:
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
print(maxDotProduct(nums1, nums2))  # Output: 18
