"""
1040. Moving Stones Until Consecutive II

Given an array of 3 or more integers representing the positions of stones on a number line, return the minimum and maximum number of moves to make the stones consecutive.

Constraints:
- 3 <= stones.length <= 10^4
- 1 <= stones[i] <= 10^9

Example:
Input: stones = [7,4,9]
Output: [1,2]
"""
from typing import List

def numMovesStonesII(stones: List[int]) -> List[int]:
    stones.sort()
    n = len(stones)
    max_moves = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
    min_moves = n
    i = 0
    for j in range(n):
        while stones[j] - stones[i] + 1 > n:
            i += 1
        if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
            min_moves = min(min_moves, 2)
        else:
            min_moves = min(min_moves, n - (j - i + 1))
    return [min_moves, max_moves]

# Example usage:
stones = [7,4,9]
print(numMovesStonesII(stones))  # Output: [1, 2]
