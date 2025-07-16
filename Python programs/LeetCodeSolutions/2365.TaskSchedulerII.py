"""
LeetCode 2365. Task Scheduler II

Given tasks and space, return the minimum days to finish all tasks.

Example:
Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= space <= tasks.length
"""

def taskSchedulerII(tasks, space):
    last = {}
    day = 0
    for t in tasks:
        if t in last and day - last[t] <= space:
            day = last[t] + space + 1
        else:
            day += 1
        last[t] = day
    return day

# Example usage:
# print(taskSchedulerII([1,2,1,2,3,1], 3))  # Output: 9
