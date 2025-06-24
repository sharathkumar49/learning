"""
LeetCode 1335. Minimum Difficulty of a Job Schedule

Given an array jobDifficulty and an integer d, split the jobs into d days such that the sum of the daily difficulties is minimized. Return the minimum sum, or -1 if not possible.

Constraints:
- 1 <= jobDifficulty.length <= 300
- 1 <= jobDifficulty[i] <= 1000
- 1 <= d <= 10

Example:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
"""
def minDifficulty(jobDifficulty, d):
    n = len(jobDifficulty)
    if n < d:
        return -1
    dp = [[float('inf')] * (n+1) for _ in range(d+1)]
    dp[0][0] = 0
    for i in range(1, d+1):
        for j in range(i, n+1):
            maxd = 0
            for k in range(j-1, i-2, -1):
                maxd = max(maxd, jobDifficulty[k])
                dp[i][j] = min(dp[i][j], dp[i-1][k] + maxd)
    return dp[d][n]

# Example usage:
jobDifficulty = [6,5,4,3,2,1]
d = 2
print(minDifficulty(jobDifficulty, d))  # Output: 7
