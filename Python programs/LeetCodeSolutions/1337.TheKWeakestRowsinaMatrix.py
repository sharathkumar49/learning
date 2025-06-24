"""
LeetCode 1337. The K Weakest Rows in a Matrix

Given a m x n matrix mat of 1s (soldiers) and 0s (civilians), return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Constraints:
- m == mat.length
- n == mat[i].length
- 2 <= n, m <= 100
- 1 <= k <= m

Example:
Input: mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3
Output: [2,0,3]
"""
def kWeakestRows(mat, k):
    power = [(sum(row), i) for i, row in enumerate(mat)]
    power.sort()
    return [i for _, i in power[:k]]

# Example usage:
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(kWeakestRows(mat, k))  # Output: [2,0,3]
