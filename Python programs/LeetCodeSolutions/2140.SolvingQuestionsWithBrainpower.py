"""
LeetCode 2140. Solving Questions With Brainpower

Given an array questions where questions[i] = [points, brainpower], return the maximum points you can earn.

Example:
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5

Constraints:
- 1 <= questions.length <= 10^5
- 1 <= points, brainpower <= 10^5
"""

def mostPoints(questions):
    n = len(questions)
    dp = [0]*(n+1)
    for i in range(n-1, -1, -1):
        points, brain = questions[i]
        dp[i] = max(points + dp[min(n, i+brain+1)], dp[i+1])
    return dp[0]

# Example usage:
# print(mostPoints([[3,2],[4,3],[4,4],[2,5]]))  # Output: 5
