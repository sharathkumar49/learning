"""
568. Maximum Vacation Days
Difficulty: Hard

You are given an m x n matrix flights representing the airline network, and an m x n matrix days representing the vacation days you can spend in each city per week.
Return the maximum vacation days you can take.

Example 1:
Input: flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12

Constraints:
2 <= m, n <= 100
flights[i][j] is 0 or 1.
days[i][j] is in the range [0, 7].
"""

def maxVacationDays(flights, days):
    m, n = len(flights), len(days[0])
    dp = [-float('inf')] * m
    dp[0] = 0
    for week in range(n):
        tmp = [-float('inf')] * m
        for i in range(m):
            for j in range(m):
                if i == j or flights[j][i]:
                    tmp[i] = max(tmp[i], dp[j] + days[i][week])
        dp = tmp
    return max(dp)

# Example usage
if __name__ == "__main__":
    print(maxVacationDays([[0,1,1],[1,0,1],[1,1,0]], [[1,3,1],[6,0,3],[3,3,3]]))  # Output: 12
