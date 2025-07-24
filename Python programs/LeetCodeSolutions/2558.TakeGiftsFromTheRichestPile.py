"""
LeetCode 2558. Take Gifts From the Richest Pile

Given piles and k, return the total number of gifts after k operations.

Constraints:
- 1 <= piles.length, k <= 10^5
"""

def pickGifts(piles, k):
    import heapq
    piles = [-x for x in piles]
    heapq.heapify(piles)
    for _ in range(k):
        x = -heapq.heappop(piles)
        heapq.heappush(piles, -int(x**0.5))
    return -sum(piles)
# Example usage:
# print(pickGifts([25,64,9,4,100], 4))  # Output: 29
