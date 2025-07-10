"""
LeetCode 1626. Best Team With No Conflicts

Given scores and ages of players, return the maximum score of a team with no conflicts. A conflict exists if a younger player has a strictly higher score than an older player.

Example 1:
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34

Constraints:
- 1 <= scores.length, ages.length <= 1000
- 1 <= scores[i] <= 10^6
- 1 <= ages[i] <= 1000
"""

def bestTeamScore(scores, ages):
    players = sorted(zip(ages, scores))
    n = len(scores)
    dp = [0]*n
    for i in range(n):
        dp[i] = players[i][1]
        for j in range(i):
            if players[j][1] <= players[i][1]:
                dp[i] = max(dp[i], dp[j] + players[i][1])
    return max(dp)

# Example usage:
# scores = [1,3,5,10,15]
# ages = [1,2,3,4,5]
# print(bestTeamScore(scores, ages))  # Output: 34
