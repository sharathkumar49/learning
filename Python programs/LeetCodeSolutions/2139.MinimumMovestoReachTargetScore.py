"""
LeetCode 2139. Minimum Moves to Reach Target Score

Given an integer target and maxDoubles, return the minimum number of moves to reach target from 1.

Example:
Input: target = 5, maxDoubles = 1
Output: 4

Constraints:
- 1 <= target <= 10^9
- 0 <= maxDoubles <= 100
"""

def minMoves(target, maxDoubles):
    moves = 0
    while target > 1 and maxDoubles:
        if target % 2 == 0:
            target //= 2
            maxDoubles -= 1
        else:
            target -= 1
        moves += 1
    return moves + target - 1

# Example usage:
# print(minMoves(5, 1))  # Output: 4
