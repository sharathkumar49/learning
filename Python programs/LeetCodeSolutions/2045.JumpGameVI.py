"""
LeetCode 2045. Jump Game VI

Given an array nums and an integer k, return the maximum score you can get by jumping at most k steps at a time.

Example:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7

Constraints:
- 1 <= nums.length, k <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def maxResult(nums, k):
    import heapq
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    heap = [(-dp[0], 0)]
    for i in range(1, n):
        while heap[0][1] < i - k:
            heapq.heappop(heap)
        dp[i] = -heap[0][0] + nums[i]
        heapq.heappush(heap, (-dp[i], i))
    return dp[-1]

# Example usage:
# print(maxResult([1,-1,-2,4,-7,3], 2))  # Output: 7
