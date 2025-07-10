"""
LeetCode 1883. Minimum Skips to Arrive at Meeting

You are given an integer array dist and an integer speed. You can skip up to k rests. Return the minimum number of skips required to arrive on time, or -1 if impossible.

Example:
Input: dist = [1,3,2], speed = 4, hoursBefore = 2
Output: 1

Constraints:
- 1 <= dist.length <= 1000
- 1 <= dist[i] <= 10^4
- 1 <= speed <= 10^6
- 1 <= hoursBefore <= 10^7
"""

import math

def minSkips(dist, speed, hoursBefore):
    n = len(dist)
    dp = [0] + [float('inf')] * n
    for d in dist:
        ndp = [float('inf')] * (n+1)
        for k in range(n):
            ndp[k] = min(ndp[k], math.ceil((dp[k] + d) / speed) * speed)
            ndp[k+1] = min(ndp[k+1], dp[k] + d)
        dp = ndp
    for k in range(n+1):
        if dp[k] <= hoursBefore * speed:
            return k
    return -1

# Example usage:
# print(minSkips([1,3,2], 4, 2))  # Output: 1
