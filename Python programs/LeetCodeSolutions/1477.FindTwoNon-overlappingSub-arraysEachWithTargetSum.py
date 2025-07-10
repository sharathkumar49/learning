"""
LeetCode 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

Given an array of integers arr and an integer target, return the minimum sum of the lengths of two non-overlapping sub-arrays each with sum equal to target. If there are no such sub-arrays, return -1.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 1000
- 1 <= target <= 10^8

Example:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
"""
def minSumOfLengths(arr, target):
    n = len(arr)
    best = [float('inf')] * n
    res = float('inf')
    left = {0: -1}
    curr = 0
    min_len = float('inf')
    for i, x in enumerate(arr):
        curr += x
        if curr - target in left:
            l = i - left[curr - target]
            min_len = min(min_len, l)
            best[i] = min_len
        else:
            best[i] = min_len
        left[curr] = i
    curr = 0
    left = {0: -1}
    min_len = float('inf')
    for i in range(n-1, -1, -1):
        curr += arr[i]
        if curr - target in left:
            l = left[curr - target] - i
            if i > 0 and best[i-1] < float('inf'):
                res = min(res, l + best[i-1])
        left[curr] = i
    return res if res < float('inf') else -1

# Example usage:
arr = [3,2,2,4,3]
target = 3
print(minSumOfLengths(arr, target))  # Output: 2
