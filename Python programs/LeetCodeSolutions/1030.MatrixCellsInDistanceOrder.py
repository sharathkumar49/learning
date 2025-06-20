"""
1030. Matrix Cells in Distance Order

Given a matrix of R rows and C columns, and a cell in that matrix (r0, c0), return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0).

Constraints:
- 1 <= R <= 100
- 1 <= C <= 100
- 0 <= r0 < R
- 0 <= c0 < C

Example:
Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances are 0 and 1 from (0,0).
"""
from typing import List

def allCellsDistOrder(R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    cells = [[r, c] for r in range(R) for c in range(C)]
    cells.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return cells

# Example usage:
R, C, r0, c0 = 1, 2, 0, 0
print(allCellsDistOrder(R, C, r0, c0))  # Output: [[0, 0], [0, 1]]
