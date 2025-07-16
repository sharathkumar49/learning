"""
LeetCode 2432. The Employee Who Worked on the Longest Task

Given logs of employee tasks, return the ID of the employee who worked the longest.

Constraints:
- 1 <= logs.length <= 10^5
"""

def hardestWorker(n, logs):
    res, max_time, prev = 0, 0, 0
    for i, t in logs:
        duration = t - prev
        if duration > max_time or (duration == max_time and i < res):
            res = i
            max_time = duration
        prev = t
    return res

# Example usage:
# print(hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))  # Output: 1
