"""
311. Sparse Matrix Multiplication

Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

Constraints:
- 1 <= m, k, n <= 100
- -100 <= mat1[i][j], mat2[i][j] <= 100
"""
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for x in range(k):
                if mat1[i][x] != 0:
                    for j in range(n):
                        if mat2[x][j] != 0:
                            res[i][j] += mat1[i][x] * mat2[x][j]
        return res

# Example usage:
mat1 = [[1,0,0],[0,0,2],[0,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(Solution().multiply(mat1, mat2))  # Output: [[7,0,0],[0,0,2],[0,0,3]]
