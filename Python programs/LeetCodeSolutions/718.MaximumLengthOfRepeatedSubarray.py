"""
LeetCode 718. Maximum Length of Repeated Subarray

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 100
"""
from typing import List

def findLength(nums1: List[int], nums2: List[int]) -> int:
    m, n = len(nums1), len(nums2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    res = 0
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i+1][j+1] + 1
                res = max(res, dp[i][j])
    return res

# Example usage
if __name__ == "__main__":
    print(findLength([1,2,3,2,1], [3,2,1,4,7]))  # Output: 3
    print(findLength([0,0,0,0,0], [0,0,0,0,0]))  # Output: 5
