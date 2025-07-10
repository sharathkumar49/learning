"""
LeetCode 1787. Make the XOR of All Segments Equal to Zero

Given an array arr and an integer k, return the minimum number of changes to make the XOR of every segment of length k equal to zero.

Example 1:
Input: arr = [1,2,0,3,0], k = 1
Output: 3

Constraints:
- 1 <= k <= arr.length <= 2000
- 0 <= arr[i] < 2^10
"""

def minChanges(arr, k):
    from collections import Counter
    n = len(arr)
    dp = [0] + [float('inf')]*((1<<10)-1)
    for i in range(k):
        count = Counter(arr[j] for j in range(i, n, k))
        total = n//k + (1 if i < n%k else 0)
        ndp = [min(dp)]*len(dp)
        for mask in range(len(dp)):
            for x in count:
                ndp[mask] = min(ndp[mask], dp[mask^x] + total - count[x])
        dp = ndp
    return dp[0]

# Example usage:
# arr = [1,2,0,3,0]
# k = 1
# print(minChanges(arr, k))  # Output: 3
