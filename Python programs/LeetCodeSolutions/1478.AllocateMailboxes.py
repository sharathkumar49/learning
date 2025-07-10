"""
LeetCode 1478. Allocate Mailboxes

Given the array houses and an integer k, allocate k mailboxes in the houses such that the total distance between each house and its nearest mailbox is minimized. Return the minimum total distance.

Constraints:
- 1 <= houses.length <= 100
- 1 <= houses[i] <= 10^4
- 1 <= k <= houses.length

Example:
Input: houses = [1,4,8,10,20], k = 3
Output: 5
"""
def minDistance(houses, k):
    houses.sort()
    n = len(houses)
    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            m = (i + j) // 2
            for l in range(i, j+1):
                cost[i][j] += abs(houses[l] - houses[m])
    dp = [[float('inf')] * (k+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            for p in range(i):
                dp[i][j] = min(dp[i][j], dp[p][j-1] + cost[p][i-1])
    return dp[n][k]

# Example usage:
houses = [1,4,8,10,20]
k = 3
print(minDistance(houses, k))  # Output: 5
