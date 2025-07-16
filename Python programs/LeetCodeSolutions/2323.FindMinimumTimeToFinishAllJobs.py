"""
LeetCode 2323. Find Minimum Time to Finish All Jobs

Given jobs and workers, return the minimum time to finish all jobs.

Example:
Input: jobs = [3,2,3], workers = [3,3,3]
Output: 3

Constraints:
- 1 <= jobs.length, workers.length <= 10^5
"""

def minimumTime(jobs, workers):
    return max(max(jobs), max(workers))

# Example usage:
# print(minimumTime([3,2,3], [3,3,3]))  # Output: 3
