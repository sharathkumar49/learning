"""
LeetCode 2247. Maximum Cost of Trip With K Edges

Given n, edges, and k, return the maximum cost of a trip with k edges.

Example:
Input: n = 5, edges = [[0,1,10],[1,2,10],[2,3,10],[3,4,10]], k = 2
Output: 20

Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= 1000
- 1 <= k <= n-1
"""

def maximumCost(n, edges, k):
    dp = [[-float('inf')]*n for _ in range(k+1)]
    dp[0][0] = 0
    for i in range(1, k+1):
        for u, v, w in edges:
            dp[i][v] = max(dp[i][v], dp[i-1][u]+w)
    return max(dp[k])

# Example usage:
# print(maximumCost(5, [[0,1,10],[1,2,10],[2,3,10],[3,4,10]], 2))  # Output: 20
