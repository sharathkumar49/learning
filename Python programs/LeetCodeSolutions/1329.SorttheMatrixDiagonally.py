"""
LeetCode 1329. Sort the Matrix Diagonally

Given a m x n matrix, sort each diagonal in ascending order and return the resulting matrix.

Constraints:
- 1 <= m, n <= 100
- 1 <= mat[i][j] <= 100

Example:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
"""
def diagonalSort(mat):
    from collections import defaultdict
    m, n = len(mat), len(mat[0])
    diags = defaultdict(list)
    for i in range(m):
        for j in range(n):
            diags[i-j].append(mat[i][j])
    for d in diags:
        diags[d].sort(reverse=True)
    for i in range(m):
        for j in range(n):
            mat[i][j] = diags[i-j].pop()
    return mat

# Example usage:
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(diagonalSort(mat))  # Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
