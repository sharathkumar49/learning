"""
LeetCode 2111. Minimum Operations to Make the Array K-Increasing

Given an array arr and an integer k, return the minimum number of operations to make arr k-increasing.

Example:
Input: arr = [5,4,3,2,1], k = 1
Output: 4

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
- 1 <= k <= arr.length
"""

def kIncreasing(arr, k):
    import bisect
    res = 0
    n = len(arr)
    for i in range(k):
        seq = [arr[j] for j in range(i, n, k)]
        dp = []
        for x in seq:
            idx = bisect.bisect_right(dp, x)
            if idx == len(dp):
                dp.append(x)
            else:
                dp[idx] = x
        res += len(seq) - len(dp)
    return res

# Example usage:
# print(kIncreasing([5,4,3,2,1], 1))  # Output: 4
