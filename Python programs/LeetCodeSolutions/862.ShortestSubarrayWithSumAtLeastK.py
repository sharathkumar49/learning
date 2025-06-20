"""
862. Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray with sum at least k. If there is no such subarray, return -1.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= 10^9
"""
def shortestSubarray(nums, k):
    from collections import deque
    n = len(nums)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    res = n + 1
    dq = deque()
    for i in range(n+1):
        while dq and prefix[i] - prefix[dq[0]] >= k:
            res = min(res, i - dq.popleft())
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()
        dq.append(i)
    return res if res <= n else -1

# Example usage:
print(shortestSubarray([1], 1))        # Output: 1
print(shortestSubarray([1,2], 4))      # Output: -1
print(shortestSubarray([2,-1,2], 3))   # Output: 3
