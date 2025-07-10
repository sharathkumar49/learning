"""
LeetCode 1906. Minimum Absolute Difference Queries

Given an integer array nums and a 2D array queries, return an array of answers for each query, where each answer is the minimum absolute difference between any two distinct numbers in the subarray.

Example:
Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
Output: [2,1,4,1]

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 100
- 1 <= queries.length <= 2 * 10^4
- 0 <= l <= r < nums.length
"""

def minDifference(nums, queries):
    n = len(nums)
    pre = [[0]*(n+1) for _ in range(101)]
    for i, x in enumerate(nums):
        for v in range(1, 101):
            pre[v][i+1] = pre[v][i] + (x == v)
    res = []
    for l, r in queries:
        arr = [v for v in range(1, 101) if pre[v][r+1] - pre[v][l] > 0]
        if len(arr) < 2:
            res.append(-1)
        else:
            res.append(min(arr[i+1] - arr[i] for i in range(len(arr)-1)))
    return res

# Example usage:
# print(minDifference([1,3,4,8], [[0,1],[1,2],[2,3],[0,3]]))  # Output: [2,1,4,1]
