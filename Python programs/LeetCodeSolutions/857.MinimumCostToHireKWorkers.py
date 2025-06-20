"""
857. Minimum Cost to Hire K Workers

There are n workers. Each worker has a quality and a minimum wage expectation. We want to hire exactly k workers to minimize the total wage. Return the least amount of money needed to hire exactly k workers.

Example 1:
Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.0

Example 2:
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667

Constraints:
- n == quality.length == wage.length
- 1 <= k <= n <= 10^4
- 1 <= quality[i], wage[i] <= 10^4
"""
import heapq

def mincostToHireWorkers(quality, wage, k):
    workers = sorted((w/q, q) for q, w in zip(quality, wage))
    res = float('inf')
    totalq = 0
    heap = []
    for ratio, q in workers:
        heapq.heappush(heap, -q)
        totalq += q
        if len(heap) > k:
            totalq += heapq.heappop(heap)
        if len(heap) == k:
            res = min(res, ratio * totalq)
    return res

# Example usage:
print(f"{mincostToHireWorkers([10,20,5], [70,50,30], 2):.5f}")  # Output: 105.0
print(f"{mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3):.5f}")  # Output: 30.66667
