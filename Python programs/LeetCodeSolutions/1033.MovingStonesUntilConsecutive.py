"""
1033. Moving Stones Until Consecutive

Three stones are on a number line at positions a, b, and c. Each turn, you pick up a stone at an endpoint and move it to an unoccupied position between the other two stones. Return the minimum and maximum number of moves to make the stones consecutive.

Constraints:
- 1 <= a <= b <= c <= 100

Example:
Input: a = 1, b = 2, c = 5
Output: [1, 2]
"""
from typing import List

def numMovesStones(a: int, b: int, c: int) -> List[int]:
    x, y, z = sorted([a, b, c])
    if z - y == 1 and y - x == 1:
        return [0, 0]
    min_moves = 1 if z - y <= 2 or y - x <= 2 else 2
    max_moves = z - x - 2
    return [min_moves, max_moves]

# Example usage:
a, b, c = 1, 2, 5
print(numMovesStones(a, b, c))  # Output: [1, 2]
