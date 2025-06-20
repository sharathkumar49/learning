"""
1039. Minimum Score Triangulation of Polygon

Given an array values of length n, return the minimum score to triangulate a polygon with n vertices, where the score of a triangle is the product of its vertices' values.

Constraints:
- 3 <= values.length <= 50
- 1 <= values[i] <= 100

Example:
Input: values = [1,2,3]
Output: 6
"""
from typing import List

def minScoreTriangulation(values: List[int]) -> int:
    n = len(values)
    dp = [[0]*n for _ in range(n)]
    for l in range(3, n+1):
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = min(dp[i][k] + dp[k][j] + values[i]*values[j]*values[k] for k in range(i+1, j))
    return dp[0][n-1]

# Example usage:
values = [1,2,3]
print(minScoreTriangulation(values))  # Output: 6
