"""
LeetCode 2174. Remove All Ones With Row and Column Flips

Given a binary matrix, return the minimum number of row and column flips to make all elements zero, or -1 if impossible.

Example:
Input: matrix = [[0,1,0],[1,0,1],[0,1,0]]
Output: 2

Constraints:
- 1 <= matrix.length, matrix[0].length <= 10
"""

def removeOnes(matrix):
    m, n = len(matrix), len(matrix[0])
    from itertools import product
    res = float('inf')
    for row_mask in range(1<<m):
        for col_mask in range(1<<n):
            mat = [[matrix[i][j] for j in range(n)] for i in range(m)]
            for i in range(m):
                if (row_mask >> i) & 1:
                    for j in range(n):
                        mat[i][j] ^= 1
            for j in range(n):
                if (col_mask >> j) & 1:
                    for i in range(m):
                        mat[i][j] ^= 1
            if all(all(x==0 for x in row) for row in mat):
                res = min(res, bin(row_mask).count('1') + bin(col_mask).count('1'))
    return res if res != float('inf') else -1

# Example usage:
# print(removeOnes([[0,1,0],[1,0,1],[0,1,0]]))  # Output: 2
