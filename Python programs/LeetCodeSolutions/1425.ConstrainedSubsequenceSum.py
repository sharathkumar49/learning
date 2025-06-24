"""
LeetCode 1425. Constrained Subsequence Sum

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, j - i <= k.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

Example:
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
"""
def constrainedSubsetSum(nums, k):
    from collections import deque
    n = len(nums)
    dp = nums[:]
    q = deque()
    for i in range(n):
        if q:
            dp[i] = max(dp[i], nums[i] + dp[q[0]])
        while q and dp[i] >= dp[q[-1]]:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
    return max(dp)

# Example usage:
nums = [10,2,-10,5,20]
k = 2
print(constrainedSubsetSum(nums, k))  # Output: 37
