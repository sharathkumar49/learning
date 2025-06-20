"""
120. Triangle
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == i + 1
- -10^4 <= triangle[i][j] <= 10^4

Example:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
"""
from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = triangle[-1][:]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    return dp[0]

# Example usage:
if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(minimumTotal(triangle))  # Output: 11
