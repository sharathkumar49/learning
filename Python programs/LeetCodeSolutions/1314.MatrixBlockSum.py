"""
LeetCode 1314. Matrix Block Sum

Given a matrix mat and an integer K, return a matrix answer where answer[i][j] is the sum of all elements mat[r][c] for i-K <= r <= i+K, j-K <= c <= j+K, and (r, c) is within the matrix.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- 0 <= mat[i][j] <= 100
- 0 <= K <= min(m, n)

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
"""
def matrixBlockSum(mat, K):
    m, n = len(mat), len(mat[0])
    ps = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            ps[i+1][j+1] = mat[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1, c1 = max(0, i-K), max(0, j-K)
            r2, c2 = min(m, i+K+1), min(n, j+K+1)
            res[i][j] = ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]
    return res

# Example usage:
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 1
print(matrixBlockSum(mat, K))  # Output: [[12,21,16],[27,45,33],[24,39,28]]
