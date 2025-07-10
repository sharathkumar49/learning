"""
LeetCode 1690. Stone Game VII

Given an array stones, return the difference in scores between Alice and Bob if both play optimally.

Example 1:
Input: stones = [5,3,1,4,2]
Output: 6

Constraints:
- 2 <= stones.length <= 1000
- 1 <= stones[i] <= 1000
"""

def stoneGameVII(stones):
    n = len(stones)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + stones[i]
    dp = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = max(prefix[j+1]-prefix[i+1]-dp[i+1][j], prefix[j]-prefix[i]-dp[i][j-1])
    return dp[0][n-1]

# Example usage:
# stones = [5,3,1,4,2]
# print(stoneGameVII(stones))  # Output: 6
