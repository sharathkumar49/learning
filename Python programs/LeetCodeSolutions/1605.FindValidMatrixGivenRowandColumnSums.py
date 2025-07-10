"""
LeetCode 1605. Find Valid Matrix Given Row and Column Sums

Given two arrays rowSum and colSum, return any matrix of non-negative integers that satisfies the given row and column sums.

Example 1:
Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],[1,7]]

Constraints:
- 1 <= rowSum.length, colSum.length <= 500
- 0 <= rowSum[i], colSum[i] <= 10^8
- sum(rowSum) == sum(colSum)
"""

def restoreMatrix(rowSum, colSum):
    m, n = len(rowSum), len(colSum)
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            v = min(rowSum[i], colSum[j])
            res[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
    return res

# Example usage:
# rowSum = [3,8]
# colSum = [4,7]
# print(restoreMatrix(rowSum, colSum))  # Output: [[3,0],[1,7]]
