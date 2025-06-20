"""
LeetCode 689. Maximum Sum of 3 Non-Overlapping Subarrays

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return the starting indices of each subarray.

Example 1:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0, 3, 5]

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= k <= nums.length / 3
"""
from typing import List

def maxSumOfThreeSubarrays(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    sum_k = [0]*(n-k+1)
    cur = sum(nums[:k])
    sum_k[0] = cur
    for i in range(1, n-k+1):
        cur += nums[i+k-1] - nums[i-1]
        sum_k[i] = cur
    left = [0]*(n-k+1)
    best = 0
    for i in range(n-k+1):
        if sum_k[i] > sum_k[best]:
            best = i
        left[i] = best
    right = [0]*(n-k+1)
    best = n-k
    for i in range(n-k, -1, -1):
        if sum_k[i] >= sum_k[best]:
            best = i
        right[i] = best
    res = None
    for j in range(k, n-2*k+1):
        i, l = left[j-k], right[j+k]
        total = sum_k[i] + sum_k[j] + sum_k[l]
        if res is None or total > res[0]:
            res = (total, [i, j, l])
    return res[1]

# Example usage
if __name__ == "__main__":
    print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))  # Output: [0, 3, 5]
