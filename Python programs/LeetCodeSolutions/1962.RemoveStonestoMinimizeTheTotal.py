"""
LeetCode 1962. Remove Stones to Minimize the Total

Given an array piles, you can perform k operations. In each operation, remove the largest pile and add back half of it. Return the minimum total after k operations.

Example:
Input: piles = [5,4,9], k = 2
Output: 12

Constraints:
- 1 <= piles.length <= 10^5
- 1 <= piles[i] <= 10^4
- 1 <= k <= 10^5
"""

import heapq

def minStoneSum(piles, k):
    h = [-x for x in piles]
    heapq.heapify(h)
    for _ in range(k):
        x = -heapq.heappop(h)
        x -= x // 2
        heapq.heappush(h, -x)
    return -sum(h)

# Example usage:
# print(minStoneSum([5,4,9], 2))  # Output: 12
