"""
LeetCode 1723. Find Minimum Time to Finish All Jobs

Given n jobs and k workers, assign jobs to minimize the maximum working time of any worker.

Example 1:
Input: jobs = [3,2,3], k = 3
Output: 3

Constraints:
- 1 <= k <= jobs.length <= 12
- 1 <= jobs[i] <= 10^7
"""

def minimumTimeRequired(jobs, k):
    jobs.sort(reverse=True)
    res = sum(jobs)
    workloads = [0] * k
    def dfs(i):
        nonlocal res
        if i == len(jobs):
            res = min(res, max(workloads))
            return
        for j in range(k):
            if workloads[j] + jobs[i] < res:
                workloads[j] += jobs[i]
                dfs(i+1)
                workloads[j] -= jobs[i]
            if workloads[j] == 0:
                break
    dfs(0)
    return res

# Example usage:
# jobs = [3,2,3]
# k = 3
# print(minimumTimeRequired(jobs, k))  # Output: 3
