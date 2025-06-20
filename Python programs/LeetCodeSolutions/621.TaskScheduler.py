"""
621. Task Scheduler
Difficulty: Medium

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU can complete either one task or be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter), that is that there must be at least n units of time between two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6

Constraints:
1 <= tasks.length <= 10^4
0 <= n <= 100
Tasks are upper-case English letters.
"""

def leastInterval(tasks, n):
    from collections import Counter
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for v in counts.values() if v == max_count)
    return max(len(tasks), (max_count - 1) * (n + 1) + num_max)

# Example usage
if __name__ == "__main__":
    print(leastInterval(["A","A","A","B","B","B"], 2))  # Output: 8
    print(leastInterval(["A","A","A","B","B","B"], 0))  # Output: 6
