"""
1074. Number of Submatrices That Sum to Target

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

Constraints:
- 1 <= matrix.length <= 100
- 1 <= matrix[0].length <= 100
- -1000 <= matrix[i][j] <= 1000
- -10^8 <= target <= 10^8

Example:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
"""
from typing import List

def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    from collections import Counter
    m, n = len(matrix), len(matrix[0])
    res = 0
    for r1 in range(m):
        sums = [0] * n
        for r2 in range(r1, m):
            for c in range(n):
                sums[c] += matrix[r2][c]
            count = Counter({0: 1})
            curr = 0
            for s in sums:
                curr += s
                res += count[curr - target]
                count[curr] += 1
    return res

# Example usage:
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
print(numSubmatrixSumTarget(matrix, target))  # Output: 4
