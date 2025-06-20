"""
308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, handle multiple queries of the following types:
- Update the value of an element in matrix.
- Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
- NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
- void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- -1000 <= matrix[i][j] <= 1000
- 0 <= row < m
- 0 <= col < n
- 0 <= row1 <= row2 < m
- 0 <= col1 <= col2 < n
- At most 2 * 10^4 calls will be made to update and sumRegion.
"""
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.nums = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def _add(self, row, col, val):
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += val
                j += j & -j
            i += i & -i

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        self._add(row, col, diff)

    def _sum(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self._sum(row2, col2) - self._sum(row1 - 1, col2)
                - self._sum(row2, col1 - 1) + self._sum(row1 - 1, col1 - 1))

# Example usage:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # Output: 8
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))  # Output: 10
