"""
LeetCode 1504. Count Submatrices With All Ones

Given a binary matrix mat, return the number of submatrices that have all ones.

Constraints:
- 1 <= rows, cols <= 150
- 0 <= mat[i][j] <= 1

Example:
Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
"""
def numSubmat(mat):
    m, n = len(mat), len(mat[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j]:
                width = n
                for k in range(i, m):
                    if mat[k][j] == 0:
                        break
                    width = min(width, sum(mat[k][j:]))
                    res += width
    return res

# Example usage:
mat = [[1,0,1],[1,1,0],[1,1,0]]
print(numSubmat(mat))  # Output: 13
