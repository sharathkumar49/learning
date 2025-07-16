"""
LeetCode 2244. Minimum Rounds to Complete All Tasks

Given tasks, return the minimum rounds to complete all tasks.

Example:
Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= tasks[i] <= 10^9
"""

def minimumRounds(tasks):
    from collections import Counter
    freq = Counter(tasks)
    res = 0
    for v in freq.values():
        if v == 1:
            return -1
        res += (v+2)//3
    return res

# Example usage:
# print(minimumRounds([2,2,3,3,2,4,4,4,4,4]))  # Output: 4
