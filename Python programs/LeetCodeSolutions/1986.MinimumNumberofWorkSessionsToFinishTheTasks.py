"""
LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks

Given an array tasks and an integer sessionTime, return the minimum number of work sessions to finish all the tasks.

Example:
Input: tasks = [1,2,3], sessionTime = 3
Output: 2

Constraints:
- 1 <= tasks.length <= 14
- 1 <= tasks[i] <= sessionTime <= 15
"""

def minSessions(tasks, sessionTime):
    n = len(tasks)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += tasks[i]
        for i in range(n):
            if not (mask & (1 << i)) and total + tasks[i] <= sessionTime:
                dp[mask | (1 << i)] = min(dp[mask | (1 << i)], dp[mask] + (total == 0))
    return dp[-1]

# Example usage:
# print(minSessions([1,2,3], 3))  # Output: 2
