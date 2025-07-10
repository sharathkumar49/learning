"""
LeetCode 1872. Stone Game VIII

You are given an integer array stones. Alice and Bob take turns, Alice always goes first. On each turn, the player removes the leftmost stone and adds its value to a running total. The game ends when only one stone remains. The player with the largest score wins. Return the maximum score difference Alice can achieve.

Example:
Input: stones = [-1,2,-3,4,-5]
Output: 5

Constraints:
- 2 <= stones.length <= 10^5
- -10^4 <= stones[i] <= 10^4
"""

def stoneGameVIII(stones):
    n = len(stones)
    for i in range(1, n):
        stones[i] += stones[i-1]
    res = stones[-1]
    for i in range(n-2, 0, -1):
        res = max(res, stones[i] - res)
    return res

# Example usage:
# print(stoneGameVIII([-1,2,-3,4,-5]))  # Output: 5
