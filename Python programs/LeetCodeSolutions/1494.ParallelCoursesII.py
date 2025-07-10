"""
LeetCode 1494. Parallel Courses II

Given an integer n and an array dependencies where dependencies[i] = [xi, yi] means you must take course xi before course yi, and an integer k, return the minimum number of semesters needed to complete all n courses. You can take at most k courses in a semester.

Constraints:
- 1 <= n <= 15
- 1 <= k <= n
- 0 <= dependencies.length <= n * (n - 1) / 2
- dependencies[i].length == 2

Example:
Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3
"""
def minNumberOfSemesters(n, dependencies, k):
    pre = [0]*n
    for u, v in dependencies:
        pre[v-1] |= 1 << (u-1)
    dp = [float('inf')] * (1<<n)
    dp[0] = 0
    for mask in range(1<<n):
        avail = [i for i in range(n) if not (mask>>i)&1 and (pre[i]&mask)==pre[i]]
        for take in combinations(avail, min(k, len(avail))):
            nxt = mask
            for i in take:
                nxt |= 1<<i
            dp[nxt] = min(dp[nxt], dp[mask]+1)
    return dp[(1<<n)-1]

from itertools import combinations
# Example usage:
n = 4
dependencies = [[2,1],[3,1],[1,4]]
k = 2
print(minNumberOfSemesters(n, dependencies, k))  # Output: 3
