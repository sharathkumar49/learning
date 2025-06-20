"""
1049. Last Stone Weight II

Given an array of stones, each stone has a positive integer weight. Each turn, take any two stones and smash them together. The result is either both stones are destroyed, or one is destroyed and the other has new weight. Return the smallest possible weight of the last remaining stone (or 0 if none remain).

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 100

Example:
Input: stones = [2,7,4,1,8,1]
Output: 1
"""
from typing import List

def lastStoneWeightII(stones: List[int]) -> int:
    total = sum(stones)
    dp = {0}
    for s in stones:
        dp |= {x + s for x in dp}
    return min(abs(total - 2*x) for x in dp)

# Example usage:
stones = [2,7,4,1,8,1]
print(lastStoneWeightII(stones))  # Output: 1
