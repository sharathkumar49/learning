"""
LeetCode 1918. Kth Smallest Subarray Sum

Given an integer array nums and an integer k, return the k-th smallest subarray sum.

Example:
Input: nums = [2,1,3], k = 4
Output: 3

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 1000
- 1 <= k <= nums.length * (nums.length + 1) / 2
"""

def kthSmallestSubarraySum(nums, k):
    n = len(nums)
    left, right = min(nums), sum(nums)
    def count_leq(x):
        cnt = 0
        curr = 0
        i = 0
        for j in range(n):
            curr += nums[j]
            while curr > x:
                curr -= nums[i]
                i += 1
            cnt += j - i + 1
        return cnt
    while left < right:
        mid = (left + right) // 2
        if count_leq(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage:
# print(kthSmallestSubarraySum([2,1,3], 4))  # Output: 3
