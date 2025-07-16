"""
LeetCode 2312. Selling Pieces of Wood

Given m, n, prices, return the maximum money you can earn by selling pieces of wood.

Example:
Input: m = 3, n = 5, prices = [[1,2,3],[2,2,4],[3,2,10]]
Output: 19

Constraints:
- 1 <= m, n <= 200
- 1 <= prices.length <= 200
"""

def sellingWood(m, n, prices):
    dp = [[0]*(n+1) for _ in range(m+1)]
    price_map = {(h,w):p for h,w,p in prices}
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = price_map.get((i,j), 0)
            for k in range(1, i//2+1):
                dp[i][j] = max(dp[i][j], dp[k][j]+dp[i-k][j])
            for k in range(1, j//2+1):
                dp[i][j] = max(dp[i][j], dp[i][k]+dp[i][j-k])
    return dp[m][n]

# Example usage:
# print(sellingWood(3, 5, [[1,2,3],[2,2,4],[3,2,10]]))  # Output: 19
