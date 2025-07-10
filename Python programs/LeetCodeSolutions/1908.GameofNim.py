"""
LeetCode 1908. Game of Nim

Given an array of stones, return true if you can win the game of Nim.

Example:
Input: stones = [1,2,3]
Output: false

Constraints:
- 1 <= stones.length <= 10^5
- 1 <= stones[i] <= 10^9
"""

def nimGame(stones):
    from functools import reduce
    return reduce(lambda x, y: x ^ y, stones) != 0

# Example usage:
# print(nimGame([1,2,3]))  # Output: False
