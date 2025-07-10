"""
LeetCode 1665. Minimum Initial Energy to Finish Tasks

Given a list of tasks, each task has actual and minimum energy required. Return the minimum initial energy required to finish all tasks.

Example 1:
Input: tasks = [[1,2],[2,4],[4,8]]
Output: 8

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= actuali <= minimumi <= 10^4
"""

def minimumEffort(tasks):
    tasks.sort(key=lambda x: x[1]-x[0], reverse=True)
    res = 0
    cur = 0
    for a, m in tasks:
        res = max(res, cur + m)
        cur += a
    return res

# Example usage:
# tasks = [[1,2],[2,4],[4,8]]
# print(minimumEffort(tasks))  # Output: 8
