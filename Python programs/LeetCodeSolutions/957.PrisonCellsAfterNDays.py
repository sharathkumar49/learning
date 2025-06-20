"""
957. Prison Cells After N Days
https://leetcode.com/problems/prison-cells-after-n-days/

There are 8 prison cells in a row, and each cell is either occupied or vacant. Each day, the state of the cells changes according to the following rules:
- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.
Given the initial state and an integer n, return the state of the prison after n days.

Constraints:
- cells.length == 8
- cells[i] is 0 or 1
- 1 <= n <= 10^9

Example:
Input: cells = [0,1,0,1,1,0,0,1], n = 7
Output: [0,0,1,1,0,0,0,0]
"""
from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        while n > 0:
            c = tuple(cells)
            if c in seen:
                n %= seen[c] - n
            seen[c] = n
            n -= 1
            cells = [0] + [int(cells[i-1] == cells[i+1]) for i in range(1, 7)] + [0]
        return cells

# Example usage
if __name__ == "__main__":
    cells = [0,1,0,1,1,0,0,1]
    n = 7
    print(Solution().prisonAfterNDays(cells, n))  # Output: [0,0,1,1,0,0,0,0]
