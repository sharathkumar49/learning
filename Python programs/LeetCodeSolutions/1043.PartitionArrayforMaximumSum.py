"""
1043. Partition Array for Maximum Sum

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has its values changed to become the maximum value of that subarray. Return the largest sum of the given array after partitioning.

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^9
- 1 <= k <= arr.length

Example:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
"""
from typing import List

def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        cur_max = 0
        for j in range(1, min(k, i) + 1):
            cur_max = max(cur_max, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + cur_max * j)
    return dp[n]

# Example usage:
arr = [1,15,7,9,2,5,10]
k = 3
print(maxSumAfterPartitioning(arr, k))  # Output: 84
