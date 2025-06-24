"""
LeetCode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

Given a m x n matrix of integers and an integer threshold, return the maximum side length of a square with sum less than or equal to threshold.

Constraints:
- 1 <= m, n <= 300
- 0 <= matrix[i][j] <= 10^4
- 0 <= threshold <= 10^5

Example:
Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
"""
def maxSideLength(mat, threshold):
    m, n = len(mat), len(mat[0])
    ps = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            ps[i+1][j+1] = mat[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
    res = 0
    for k in range(1, min(m, n)+1):
        for i in range(m-k+1):
            for j in range(n-k+1):
                total = ps[i+k][j+k] - ps[i][j+k] - ps[i+k][j] + ps[i][j]
                if total <= threshold:
                    res = k
    return res

# Example usage:
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4
print(maxSideLength(mat, threshold))  # Output: 2
