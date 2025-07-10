"""
LeetCode 1547. Minimum Cost to Cut a Stick

Given a stick of length n and an array cuts, return the minimum total cost to cut the stick. The cost of a cut is the length of the stick being cut.

Constraints:
- 2 <= n <= 10^6
- 1 <= cuts.length <= min(100, n-1)
- 1 <= cuts[i] < n

Example:
Input: n = 7, cuts = [1,3,4,5]
Output: 16
"""
def minCost(n, cuts):
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)
    dp = [[0]*m for _ in range(m)]
    for l in range(2, m):
        for i in range(m-l):
            j = i + l
            dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i+1, j)) + cuts[j] - cuts[i]
    return dp[0][m-1]

# Example usage:
n = 7
cuts = [1,3,4,5]
print(minCost(n, cuts))  # Output: 16
