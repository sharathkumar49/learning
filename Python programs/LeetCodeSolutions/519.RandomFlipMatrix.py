"""
519. Random Flip Matrix

You are given the number of rows m and columns n of a matrix. Write a function flip which randomly selects an integer coordinate (row, col) in the matrix that is still 0 and flips it to 1. Once a cell is flipped, it can't be flipped again. Implement a function reset to reset the matrix.

Constraints:
- 1 <= m, n <= 10^4
- At most 1000 calls will be made to flip and reset.

Example:
Input: m = 2, n = 3
Output: [0,1]
"""

import random

class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.reset()
    def flip(self) -> list:
        x = random.randint(0, self.total - 1)
        while x in self.used:
            x = random.randint(0, self.total - 1)
        self.used.add(x)
        return [x // self.n, x % self.n]
    def reset(self) -> None:
        self.used = set()

# Example usage:
sol = Solution(2, 3)
print(sol.flip())  # Output: e.g. [0, 1]
sol.reset()
