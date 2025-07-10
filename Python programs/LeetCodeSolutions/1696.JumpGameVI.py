"""
LeetCode 1696. Jump Game VI

Given an array of integers nums and an integer k, you can jump at most k steps forward from index i to index i + 1, ..., i + k. Each time you land on an index, you get nums[i] points.

Return the maximum score you can get to reach the last index.

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps as follows: 1 -> -1 -> 4 -> 3

Constraints:
- 1 <= nums.length, k <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

import collections

def maxResult(nums, k):
    dq = collections.deque([0])
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
        dp[i] = nums[i] + dp[dq[0]]
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        dq.append(i)
    return dp[-1]

# Example usage:
# nums = [1,-1,-2,4,-7,3], k = 2
# print(maxResult(nums, k))  # Output: 7
