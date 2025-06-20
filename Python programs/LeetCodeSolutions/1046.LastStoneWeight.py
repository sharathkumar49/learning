"""
1046. Last Stone Weight

You are given an array of integers stones where each element is the weight of a stone. On each turn, take the two heaviest stones and smash them together. If they are equal, both are destroyed; if not, the smaller is destroyed and the larger is replaced by the difference. Return the weight of the last remaining stone, or 0 if none remain.

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

Example:
Input: stones = [2,7,4,1,8,1]
Output: 1
"""
from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        a = -heapq.heappop(stones)
        b = -heapq.heappop(stones)
        if a != b:
            heapq.heappush(stones, -(a - b))
    return -stones[0] if stones else 0

# Example usage:
stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))  # Output: 1
