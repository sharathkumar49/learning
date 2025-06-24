"""
1136. Parallel Courses

There are n courses and prerequisites[i] = [a, b] means to take course a you must first take course b. Return the minimum number of semesters to finish all courses, or -1 if impossible.

Constraints:
- 1 <= n <= 5000
- 1 <= prerequisites.length <= 5000
- 1 <= a, b <= n

Example:
Input: n = 3, prerequisites = [[1,3],[2,3]]
Output: 2

"""
def minimumSemesters(n, relations):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0]*(n+1)
    for u, v in relations:
        graph[v].append(u)
        indegree[u] += 1
    q = deque([i for i in range(1, n+1) if indegree[i] == 0])
    semester = 0
    taken = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            taken += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        semester += 1
    return semester if taken == n else -1

# Example usage
if __name__ == "__main__":
    print(minimumSemesters(3, [[1,3],[2,3]]))  # Output: 2
