# Turing: Course Schedule
# There are a total of numCourses you have to take, labeled from 0 to numCourses-1. Some courses may have prerequisites. Return if it is possible to finish all courses.
from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return count == numCourses

if __name__ == "__main__":
    print(can_finish(2, [[1,0]]))        # Output: True
    print(can_finish(2, [[1,0],[0,1]])) # Output: False
