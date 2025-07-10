"""
LeetCode 2050. Parallel Courses III

Given n courses, some of which have prerequisites, and the time to complete each course, return the minimum time to complete all courses.

Example:
Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
Output: 8

Constraints:
- 1 <= n <= 5 * 10^4
- 1 <= time[i] <= 10^4
"""

def minimumTime(n, relations, time):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in relations:
        graph[u-1].append(v-1)
        indegree[v-1] += 1
    dp = time[:]
    q = deque([i for i in range(n) if indegree[i] == 0])
    while q:
        u = q.popleft()
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + time[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return max(dp)

# Example usage:
# print(minimumTime(3, [[1,3],[2,3]], [3,2,5]))  # Output: 8
