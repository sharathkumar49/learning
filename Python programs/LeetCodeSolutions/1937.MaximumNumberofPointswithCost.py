"""
LeetCode 1937. Maximum Number of Points with Cost

Given a matrix points, return the maximum number of points you can obtain.

Example:
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9

Constraints:
- m == points.length
- n == points[i].length
- 1 <= m, n <= 10^5
- 1 <= points[i][j] <= 10^5
"""

def maxPoints(points):
    m, n = len(points), len(points[0])
    dp = points[0][:]
    for i in range(1, m):
        left = [0]*n
        right = [0]*n
        left[0] = dp[0]
        for j in range(1, n):
            left[j] = max(left[j-1]-1, dp[j])
        right[-1] = dp[-1]
        for j in range(n-2, -1, -1):
            right[j] = max(right[j+1]-1, dp[j])
        for j in range(n):
            dp[j] = points[i][j] + max(left[j], right[j])
    return max(dp)

# Example usage:
# print(maxPoints([[1,2,3],[1,5,1],[3,1,1]]))  # Output: 9
