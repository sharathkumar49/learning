# Amazon: Course Schedule (Detect Cycle in Directed Graph)
def can_finish(numCourses, prerequisites):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return count == numCourses

if __name__ == "__main__":
    n = int(input("Number of courses: "))
    m = int(input("Number of prerequisites: "))
    prerequisites = [tuple(map(int, input().split())) for _ in range(m)]
    print("Can finish:", can_finish(n, prerequisites))
