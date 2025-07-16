"""
LeetCode 2329. Sort the Matrix Diagonally

Given mat, return the matrix with each diagonal sorted in ascending order.

Example:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:
- 1 <= mat.length, mat[0].length <= 100
"""

def diagonalSort(mat):
    from collections import defaultdict
    m, n = len(mat), len(mat[0])
    diags = defaultdict(list)
    for i in range(m):
        for j in range(n):
            diags[i-j].append(mat[i][j])
    for k in diags:
        diags[k].sort(reverse=True)
    for i in range(m):
        for j in range(n):
            mat[i][j] = diags[i-j].pop()
    return mat

# Example usage:
# print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))  # Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
